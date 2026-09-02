# Roman to Integer

<span class="pill easy">Easy</span> <span class="pill done">Solved</span> <span class="pill">Hash map</span> <span class="pill">String</span>

[Open on LeetCode :material-open-in-new:](https://leetcode.com/problems/roman-to-integer/){ .md-button }

---

## The question

Roman numerals use seven symbols:

| Symbol | I | V | X | L | C | D | M |
|---|---|---|---|---|---|---|---|
| Value | 1 | 5 | 10 | 50 | 100 | 500 | 1000 |

They are normally written largest to smallest, left to right. But four is not `IIII`, it is `IV`: the one sits **before** the five, so it is subtracted. Same for nine, `IX`.

There are exactly **six** subtractive cases:

* `I` before `V` and `X` makes 4 and 9
* `X` before `L` and `C` makes 40 and 90
* `C` before `D` and `M` makes 400 and 900

=== "Example 1"

    ```text
    Input:  s = "III"
    Output: 3
    ```

=== "Example 2"

    ```text
    Input:  s = "LVIII"
    Output: 58
    L = 50, V = 5, III = 3
    ```

=== "Example 3"

    ```text
    Input:  s = "MCMXCIV"
    Output: 1994
    M = 1000, CM = 900, XC = 90, IV = 4
    ```

---

<div class="step-row">
  <div class="step-chip s1">1 · Plan<small>say it in English</small></div>
  <div class="step-chip s2">2 · Pseudocode<small>shape before syntax</small></div>
  <div class="step-chip s3">3 · First draft<small>three syntax errors</small></div>
  <div class="step-chip s4">4 · Working code<small>then check the complexity</small></div>
</div>

## 1 · Plan

!!! plan "What is actually being asked"

    Convert a Roman numeral string to an integer.

    First thought: handle the six subtractive exceptions separately, then handle the plain largest-first numerals. Two bits of logic.

    Then: put everything in a **dict** and do a lookup. A dict answers "what is this worth" in `O(1)`.

    Then the bit that made it click. The exceptions are not a special case at all if the dict holds them too:

    > Is `s[i:i+2]`, a two character slice, in my dict? If yes, take 2 and jump the index forward by 2. If no, take 1 and jump by 1.

    One dict, **thirteen** entries. Seven singles plus the six subtractive pairs. The lookup order does all the work, because a two character window is only ever a key when it really is one of the six exceptions.

!!! insight "The one idea to remember"

    When a problem has a handful of named exceptions, ask whether the exceptions can go **in the same lookup table** as the normal cases. Very often the "special case" branch disappears entirely and what is left is one loop.

**Walking `MCMXCIV`**

| i | window `s[i:i+2]` | in dict? | counted | i becomes |
|---|---|---|---|---|
| 0 | `MC` | no | `M` = 1000 | 1 |
| 1 | `CM` | **yes** | 900 | 3 |
| 3 | `XC` | **yes** | 90 | 5 |
| 5 | `IV` | **yes** | 4 | 7 |
| 7 | past the end, loop stops | | **1994** | |

## 2 · Pseudocode

!!! pseudo "Shape"

    ```text
    build a dict of the 7 singles and the 6 subtractive pairs
    num = 0
    i = 0

    while i is inside the string
        if the two character window is a key
            add its value to num
            i += 2
        else
            add the value of the single character to num
            i += 1

    return num
    ```

## 3 · First draft, and the three things wrong with it

!!! attempt "What I wrote first"

    ```python
    roman_nums = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40,
        "IC": 90,                      # (1) should be XC
        "CD": 400, "CM": 900
    }

    num = 0
    i = 0

    while i < len(s):
        if s[i:i+2] in roman_nums:
            roman_nums.value() + num   # (2) not a method, and nothing is assigned
            i += 2
        else:
            roman_nums.value() + num   # (3) also never moves i, infinite loop
    return num
    ```

!!! gotcha "Three drafting slips"

    1. **`"IC": 90` should be `"XC"`.** Ninety is ten before a hundred. Worth a second look only because it does not crash: `XC` simply would not be found, so it falls to the single character branch and gives `10 + 100 = 110`.
    2. **`.value()` is not a dict method.** It is `.values()`, and even that returns *all* the values as a view rather than a single one. One value out of a dict is `roman_nums[s[i]]`. Also, `x + num` on its own line computes a number and throws it away. The accumulating line has to be `num += ...`.
    3. **`roman_nums[key] += num` is backwards.** `a += b` means `a = a + b`, so whatever sits on the left is the thing being built up. That version adds `num` into the dict and leaves `num` at `0`.

## 4 · Working code

!!! optimise "Final, `O(n)` time, `O(1)` space"

    ```python
    class Solution:
        def romanToInt(self, s: str) -> int:
            roman_nums = {
                "I": 1,   "V": 5,   "X": 10,  "L": 50,
                "C": 100, "D": 500, "M": 1000,
                "IV": 4,  "IX": 9,
                "XL": 40, "XC": 90,
                "CD": 400, "CM": 900
            }

            num = 0
            i = 0

            while i < len(s):
                if s[i:i+2] in roman_nums:      # a real subtractive pair
                    num += roman_nums[s[i:i+2]]
                    i += 2
                else:                           # an ordinary single symbol
                    num += roman_nums[s[i]]
                    i += 1

            return num
    ```

    Checked against every valid numeral from 1 to 3999. All correct.

!!! plan "Why `while i < len(s)` never goes out of range"

    Python is zero indexed, so a string of length 4 has indices `0, 1, 2, 3`. Starting at `0` and stopping when `i` reaches `len(s)` covers exactly those and no more.

    The part that looks risky is `s[i:i+2]` on the **last** character, where `i+2` is past the end. That is fine, because **slicing never raises**, it just returns what is there:

    ```python
    >>> "III"[2:4]
    'I'          # a one character string, so it cannot be a two character key
    >>> "III"[3]
    IndexError: string index out of range
    ```

    So the window quietly becomes a one character string, fails the `in` check, and falls to the single character branch. Slicing forgives, indexing does not.

## 5 · Complexity

!!! optimise "`O(n)` time, `O(1)` space, and that is the floor"

    **Time is `O(n)`.** The `while` loop advances `i` by 1 or 2 every pass, so it runs at most `n` times, and everything inside it is a constant time dict lookup.

    **This cannot be improved.** Every character has to be read at least once to know what the number is, so `O(n)` is the lower bound, not just what this solution happens to achieve. Naming *why* no better complexity exists is a stronger answer than naming the complexity alone.

    **Space is `O(1)`.** Not because it is a hash map, but because that hash map holds **thirteen entries no matter what the input is**. A million character input still gets the same thirteen entries. Nothing in the solution grows with `n`.

!!! plan "The precise reason for the `O(1)`"

    The dict is the thing **using** memory here, not what saves it. The space stays constant because nothing per-character is ever built: no list of parsed values, no split string, and the table is a fixed thirteen entries whatever the input.

    Phrasing: `O(1)` **because the table is fixed size**. LeetCode percentiles move around between submissions of identical code, so the reasoning is the durable part, not the number.

## Alternative worth knowing

??? note "One pass over single characters, seven keys instead of thirteen"

    The other standard solution never looks at pairs. It walks single characters and asks: is this symbol **smaller than the one after it**? If so it is the front half of a subtractive pair, so subtract it instead of adding it.

    ```python
    class Solution:
        def romanToInt(self, s: str) -> int:
            value = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}
            total = 0
            for i in range(len(s)):
                if i + 1 < len(s) and value[s[i]] < value[s[i + 1]]:
                    total -= value[s[i]]
                else:
                    total += value[s[i]]
            return total
    ```

    `MCMXCIV` becomes `1000 - 100 + 1000 - 10 + 100 - 1 + 5`, which is `1994`.

    Same `O(n)` time and `O(1)` space. Smaller table, but it encodes the subtractive rule as **logic** rather than **data**. The thirteen entry version is more explicit about what the six exceptions are, which is arguably easier to defend out loud. Either works, as long as the choice has a reason behind it.

---

## Next time

* **Put the exceptions in the lookup table.** If a problem lists a small fixed set of special cases, try making them ordinary entries in the same dict. The special case branch often disappears.
* `.values()` returns **all** the values. `d[key]` returns **one**. Different jobs.
* `a += b` means `a = a + b`, so the accumulator goes on the **left**.
* **Slicing never raises, indexing does.** `s[i:i+2]` past the end returns a short string. `s[i]` past the end is an `IndexError`. That difference is doing real work in this solution.
* When the complexity cannot be improved, say **why**. "Every character has to be read, so `O(n)` is the floor" beats "it is `O(n)`."
