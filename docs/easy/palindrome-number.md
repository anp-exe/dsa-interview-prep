# Palindrome Number

<span class="pill easy">Easy</span> <span class="pill done">Solved</span> <span class="pill">Maths</span> <span class="pill">Two pointers</span>

[Open on LeetCode :material-open-in-new:](https://leetcode.com/problems/palindrome-number/){ .md-button }

---

## The question

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

=== "Example 1"

    ```text
    Input:  x = 121
    Output: true
    Reads as 121 forwards and 121 backwards.
    ```

=== "Example 2"

    ```text
    Input:  x = -121
    Output: false
    Forwards it is -121, backwards it is 121-, so no.
    ```

=== "Example 3"

    ```text
    Input:  x = 10
    Output: false
    Backwards it is 01, so no.
    ```

**Follow up:** can you solve it without converting the integer to a string?

---

<div class="step-row">
  <div class="step-chip s1">1 · Plan<small>say it in English</small></div>
  <div class="step-chip s2">2 · Pseudocode<small>shape before syntax</small></div>
  <div class="step-chip s3">3 · First pass<small>strings, get it working</small></div>
  <div class="step-chip s4">4 · Optimise<small>numerically, O(1) space</small></div>
</div>

## 1 · Plan

!!! plan "What is actually being asked"

    Reverse the number. If the reverse equals the original, it is a palindrome.

    Edge cases to handle before anything else:

    * **Negatives are never palindromes.** The minus sign is only on one end.
    * **Anything ending in 0 is never a palindrome**, except `0` itself, because the reverse would need a leading zero.
    * Single digits are always palindromes.

    The cheap route is to turn it into a string and slice it backwards. The follow up is hinting that there is a way to do it in pure arithmetic, so expect a second pass.

## 2 · Pseudocode

!!! pseudo "String version"

    ```text
    original = string of x
    reversed = original read backwards

    if original == reversed
        return true
    else
        return false
    ```

## 3 · First pass, strings

!!! attempt "The version I wrote"

    ```python
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            original = str(x)
            backwards = original[::-1]

            if original == backwards:
                return True
            else:
                return False
    ```

    This passes. Time `O(log x)`, because a number has about `log₁₀(x)` digits and each digit gets touched a constant number of times. Space `O(log x)`, because both strings are held in memory.

!!! plan "Three fixes from the draft"

    1. **`true` and `false` are not Python.** It is `True` and `False`, capitalised. Lowercase raises `NameError`.
    2. **Do not name a variable `reversed`.** That shadows the built in `reversed()` function. Use `backwards`, `rev`, anything else.
    3. **`if cond: return True else: return False` is just `return cond`.** The whole method collapses to one line:

    ```python
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            return str(x) == str(x)[::-1]
    ```

    Same complexity, far less to read.

## 4 · Optimise

!!! insight "The one idea to remember"

    The whole reversed number is never needed. Reverse **only the back half** and compare it to what is left of the front half. Halfway through, the two meet, which also dodges any integer overflow in languages that have it.

!!! optimise "Half reversal, `O(1)` space"

    ```python
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            if x < 0 or (x % 10 == 0 and x != 0):
                return False

            reverted = 0
            while x > reverted:
                reverted = reverted * 10 + x % 10   # push last digit of x onto reverted
                x //= 10                            # drop last digit of x

            return x == reverted or x == reverted // 10
    ```

    **Line by line**

    * `x < 0` filters negatives. `x % 10 == 0 and x != 0` filters trailing zeros such as `10`, `120`, `4500`.
    * `x % 10` grabs the last digit. `reverted * 10 + digit` shifts everything left and appends it. `x //= 10` chops that digit off the original.
    * The loop stops the moment `reverted` catches up to `x`, which is the midpoint.
    * **Even digit count**, `1221`: after two turns `x = 12` and `reverted = 12`, so `x == reverted` is true.
    * **Odd digit count**, `12321`: it ends with `x = 12` and `reverted = 123`. The middle digit `3` does not need to match anything, so `reverted // 10` strips it and `12 == 12` is true.

    | | Time | Space |
    |---|---|---|
    | String slice | `O(log x)` | `O(log x)` |
    | Half reversal | `O(log x)` | `O(1)` |

    Same time class, but no extra memory allocated. That is the whole win, and the point to state explicitly.

!!! plan "Indentation in the handwritten draft"

    In the version I wrote out by hand, everything after `return False` was tucked **inside** the `if`, so the reversal only ran for numbers that had already been rejected. The guard clause must return and then the rest of the function continues at the same level as the `if`. Worth re reading indentation before submitting.

---

## Next time

* Write the edge case guards first, before the main logic. Negatives and trailing zeros were both catchable in ten seconds of thinking.
* `return condition` instead of `if condition: return True else: return False`.
* When a follow up says "without converting to a string", the answer is almost always `% 10` to peel digits off the end and `// 10` to shorten the number.
