# Easy

<span class="pill easy">3 solved</span>

The foundation set. Every one of these hides a pattern that shows up again three difficulty levels later, so the point is not to pass the test cases, it is to be able to name the pattern afterwards.

<div class="grid cards" markdown>

-   **[Two Sum](two-sum.md)**

    ---

    Flip "which two numbers add to target" into "have I already seen the complement". Nested loop becomes one pass.

    <span class="pill">Hash map</span> `O(n)`

-   **[Palindrome Number](palindrome-number.md)**

    ---

    Peel digits with `% 10` and `// 10`. Reverse only the back half so you never allocate anything.

    <span class="pill">Digit arithmetic</span> `O(1)` space

-   **[Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)**

    ---

    You do not want the global minimum, you want the best minimum **so far**. Running state in one pass.

    <span class="pill">Greedy</span> `O(n)`

</div>

## What these three taught me

| Lesson | Came from |
|---|---|
| A hash map turns "have I seen this" into `O(1)`, which kills a nested loop | Two Sum |
| Write the edge case guards before the main logic | Palindrome Number |
| `return condition`, never `if cond: return True else: return False` | Palindrome Number |
| Test a new idea against a small adversarial case on paper first | Best Time to Buy and Sell Stock |
| `log` complexity comes from **halving**, not just from looping | Best Time to Buy and Sell Stock |
| `enumerate` instead of hand rolled index counters | Two Sum |

## Suggested next

Still easy, but each one stretches a different muscle:

- [ ] Valid Parentheses, stacks
- [ ] Merge Two Sorted Lists, linked lists and two pointers
- [ ] Contains Duplicate, sets, a one liner once Two Sum has clicked
- [ ] Valid Anagram, counting with a hash map
- [ ] Maximum Subarray, running state again, sets up Kadane and DP
- [ ] Binary Search, the source of every `O(log n)`
