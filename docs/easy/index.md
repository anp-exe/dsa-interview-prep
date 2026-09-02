# Easy

<span class="pill easy">6 solved</span>

The foundation set. Every one of these hides a pattern that shows up again three difficulty levels later, so the point is not to pass the test cases, it is to be able to name the pattern afterwards.

<div class="grid cards" markdown>

-   **[Two Sum](two-sum.md)**

    ---

    Flip "which two numbers add to target" into "have I already seen the complement". Nested loop becomes one pass.

    <span class="pill">Hash map</span> `O(n)`

-   **[Palindrome Number](palindrome-number.md)**

    ---

    Peel digits with `% 10` and `// 10`. Reverse only the back half so nothing is allocated.

    <span class="pill">Digit arithmetic</span> `O(1)` space

-   **[Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)**

    ---

    Not the global minimum. The best minimum **so far**. Running state in one pass.

    <span class="pill">Greedy</span> `O(n)`

-   **[Roman to Integer](roman-to-integer.md)**

    ---

    Put the six subtractive exceptions **in** the lookup table and the special case branch disappears.

    <span class="pill">Hash map</span> `O(1)` space

-   **[Longest Common Prefix](longest-common-prefix.md)**

    ---

    Scan columns, not rows. Compare index `i` across every word before moving to `i + 1`.

    <span class="pill">Vertical scan</span> `O(S)`

-   **[Valid Parentheses](valid-parentheses.md)**

    ---

    The most recently opened bracket must close first. That is LIFO, which is a stack.

    <span class="pill">Stack</span> `O(n)`

</div>

## What these six taught me

| Lesson | Came from |
|---|---|
| A hash map turns "have I seen this" into `O(1)`, which kills a nested loop | Two Sum |
| Write the edge case guards before the main logic | Palindrome Number |
| `return condition`, never `if cond: return True else: return False` | Palindrome Number |
| Test a new idea against a small adversarial case on paper first | Best Time to Buy and Sell Stock |
| `log` complexity comes from **halving**, not just from looping | Best Time to Buy and Sell Stock |
| A list built only to call `max()` on it at the end is `O(n)` space that is not needed | Best Time to Buy and Sell Stock |
| Fix correctness first, shrink the space second. Two separate edits | Best Time to Buy and Sell Stock |
| Exceptions can live in the same lookup table as the normal cases | Roman to Integer |
| Slicing never raises, indexing does. `s[i:i+2]` past the end is safe | Roman to Integer |
| Anything inside a `while` condition re-runs every iteration | Longest Common Prefix |
| `min(gen)` allocates nothing, `min([list comp])` builds the whole list | Longest Common Prefix |
| A rule about **order** cannot be checked with `in`. Order needs a structure | Valid Parentheses |
| Repeated `elif` branches differing only by a value are a lookup table | Valid Parentheses |
| Complexity is the **worst case**, so find the input that works it hardest | Valid Parentheses |
| `enumerate` instead of hand rolled index counters | Two Sum |

## Suggested next

Still easy, but each one stretches a different muscle:

- [ ] Merge Two Sorted Lists, linked lists and two pointers
- [ ] Contains Duplicate, sets, a one liner once Two Sum has clicked
- [ ] Valid Anagram, counting with a hash map
- [ ] Maximum Subarray, running state again, sets up Kadane and DP
- [ ] Binary Search, the source of every `O(log n)`
