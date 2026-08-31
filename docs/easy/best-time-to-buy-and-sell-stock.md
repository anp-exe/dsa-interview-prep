# Best Time to Buy and Sell Stock

<span class="pill easy">Easy</span> <span class="pill done">Solved</span> <span class="pill">Greedy</span> <span class="pill">Running min</span>

[Open on LeetCode :material-open-in-new:](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/){ .md-button }

---

## The question

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.

Pick **one day to buy** and a **later day to sell** to maximise profit. Return the maximum profit, or `0` if no profit is possible.

=== "Example 1"

    ```text
    Input:  prices = [7,1,5,3,6,4]
    Output: 5
    Buy on day 2 at 1, sell on day 5 at 6, profit 5.
    ```

=== "Example 2"

    ```text
    Input:  prices = [7,6,4,3,1]
    Output: 0
    Prices only fall, so no transaction is made.
    ```

---

<div class="step-row">
  <div class="step-chip s1">1 · Plan<small>say it in English</small></div>
  <div class="step-chip s2">2 · Pseudocode<small>shape before syntax</small></div>
  <div class="step-chip s3">3 · Failed attempt<small>155 / 213 and why</small></div>
  <div class="step-chip s4">4 · Optimise<small>one pass running min</small></div>
</div>

## 1 · Plan

!!! plan "What is actually being asked"

    Buy low, sell high, and **you cannot go backwards in time**. The sell day must come after the buy day.

    First instinct: for every day, look forward at every later day and record the difference. Keep the biggest. That is every pair, so `O(n²)`.

    Second instinct, and the one that turned out to be wrong: find the smallest price in the whole array, then find the largest price after it. That feels right, and it is wrong. See below.

    Edge case: if prices only ever fall, such as `[4,3,2,1]`, every difference is negative, so return `0` rather than a loss.

## 2 · Pseudocode

!!! pseudo "Brute force shape"

    ```text
    best = 0
    for each buy day i
        for each sell day j after i
            profit = prices[j] - prices[i]
            if profit > best
                best = profit
    return best
    ```

    Correct, but `O(n²)`, and with `n` up to 100,000 it times out.

## 3 · The attempt that failed

!!! attempt "155 / 213 test cases"

    ```python
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            min_value = min(prices)
            profit = []
            i = prices.index(min(prices))
            prices = prices[i:]

            for price in prices:
                if price - min_value >= 0:
                    profit.append(price - min_value)

            max_num = max(profit)
            return max_num if max_num >= 0 else 0
    ```

    **Why it fails.** It assumes the best trade always starts at the **global** minimum. It does not.

    ```text
    prices = [2, 100, 1]

    global min = 1, at index 2
    everything after index 2 = []
    so this code returns 0

    correct answer = 98   (buy at 2, sell at 100)
    ```

    The global minimum arriving late in the array destroys a huge earlier profit that the code never even looks at.

    It is also slow for a second reason: `min()`, `.index()` and the slice each walk the list, so there are several full passes where one would do.

## 4 · Optimise

!!! insight "The one idea to remember"

    You do not need the **global** minimum. You need the **best minimum so far**.

    Walk forward once. At each day ask one question: *if I sold today, having bought at the cheapest price I have seen up to now, what would I make?* Keep the best answer. Update the cheapest price as you go. The "cannot sell before you buy" rule is enforced for free, because the running minimum only ever contains earlier days.

!!! optimise "One pass, `O(n)` time, `O(1)` space"

    ```python
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            min_price = float("inf")
            best = 0

            for price in prices:
                if price < min_price:
                    min_price = price          # new cheapest buy day so far
                elif price - min_price > best:
                    best = price - min_price   # new best sale, given that buy day

            return best
    ```

    **Trace on `[7,1,5,3,6,4]`**

    | price | min_price | profit today | best |
    |---|---|---|---|
    | 7 | 7 | . | 0 |
    | 1 | 1 | . | 0 |
    | 5 | 1 | 4 | 4 |
    | 3 | 1 | 2 | 4 |
    | 6 | 1 | 5 | **5** |
    | 4 | 1 | 3 | 5 |

    **Trace on `[2,100,1]`**, the case that broke the earlier version

    | price | min_price | profit today | best |
    |---|---|---|---|
    | 2 | 2 | . | 0 |
    | 100 | 2 | 98 | **98** |
    | 1 | 1 | . | 98 |

    `best` starts at `0` and only ever grows, so a strictly falling array returns `0` without any special casing.

    | | Time | Space |
    |---|---|---|
    | Brute force | `O(n²)` | `O(1)` |
    | Global min then max after | broken | `O(n)` |
    | Running minimum | `O(n)` | `O(1)` |

!!! gotcha "The complexity guess in my notes"

    I wrote `log(x)` as a guess. It is not. Nothing here halves the input, which is what produces a logarithm. One pass over `n` items is `O(n)`, full stop. Rule of thumb: `log` shows up when you repeatedly **halve** something, such as binary search or a balanced tree.

---

## Next time

* When a problem forbids going backwards in time, think **running state**: running min, running max, running sum. That is usually the `O(n)` unlock.
* Test an idea against a small adversarial case before writing it. `[2, 100, 1]` would have killed the global minimum idea in fifteen seconds on paper.
* Multiple calls to `min()`, `.index()` and slicing are multiple full scans. If the answer needs one pass, write one loop.
