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
    Buying on day 2 and selling on day 1 is not allowed.
    You must buy before you sell.
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
  <div class="step-chip s4">4 · Optimise<small>logic first, then space</small></div>
</div>

## 1 · Plan

!!! plan "What is actually being asked"

    Buy low, sell high, and **you cannot go backwards in time**. The sell day must come after the buy day.

    First instinct: for every day, look forward at every later day and record the difference. Keep the biggest. That is every pair, so `O(n²)`.

    Second instinct, and the one that turned out to be wrong: find the smallest price in the whole array, then find the largest price after it. It feels right. It is not.

    Edge case: if prices only ever fall, such as `[4,3,2,1]`, every difference is negative. You only lose money buying in on any day, so return `0`.

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

    A global minimum that shows up **late** wipes out a big profit earlier in the array that the code never even looks at.

    It is also slow for a second reason: `min()`, `.index()` and the slice each walk the list, so that is several full passes where one would do.

## 4 · Optimise, part one: fix the logic

!!! insight "A running minimum, not a global one"

    The global minimum is a fact about the **whole** array, including days that have not happened yet. Using it means you can end up trying to sell at a price that comes **before** the day you bought, which is time travel.

    So instead of one fixed minimum, carry a minimum that **updates as you walk forward**. Start it at infinity so the very first price always beats it, then at every day ask one question:

    > If I sold today, having bought at the cheapest price I have seen **so far**, what would I make?

    The rule enforces itself. The running minimum only ever contains days that have already happened, so you can never buy from the future.

!!! optimise "Correct, `O(n)` time, `O(n)` space"

    ```python
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            min_value = float("inf")
            profit = []

            for price in prices:
                min_value = min(min_value, price)   # cheapest seen so far
                profit.append(price - min_value)    # what today would earn

            return max(profit)
    ```

    This passes every test. `min(min_value, price)` returns whichever of the two is smaller, so `min_value` only ever goes down.

    Note that `price - min_value` can never be negative here, because `min_value` has already been updated to be at most `price`. So the old `if max_num >= 0` check was never doing anything.

    Still `O(n)` **space** though, because that list holds one entry per day.

## 5 · Optimise, part two: fix the space

!!! insight "You never need the whole list, only the champion"

    `max(a, b)` returns exactly **one** value, the bigger of the two. Think of it as a running competition:

    ```text
    max(0, 4)  ->  4     4 wins
    max(4, 2)  ->  4     4 holds on
    max(4, 5)  ->  5     new champion
    ```

    So `max_profit` is just the current champion, challenged once per day. There is no reason to keep every previous challenger around in a list.

!!! optimise "Final, `O(n)` time, `O(1)` space"

    ```python
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            min_value = float("inf")
            max_profit = 0

            for price in prices:
                min_value = min(min_value, price)              # cheapest buy day so far
                potential_profit = price - min_value           # what selling today earns
                max_profit = max(max_profit, potential_profit) # keep the champion

            return max_profit
    ```

    Two variables instead of a list. Same answer, constant memory.

    | Version | Time | Space | Correct? |
    |---|---|---|---|
    | Brute force, every pair | `O(n²)` | `O(1)` | yes, but times out |
    | Global min then max after | `O(n)` | `O(n)` | **no**, 155 / 213 |
    | Running min, list of profits | `O(n)` | `O(n)` | yes |
    | Running min, running max | `O(n)` | `O(1)` | yes |

!!! gotcha "Three things to tidy in the final version"

    1. **The trailing `if max_profit >= 0` is dead code.** `max_profit` starts at `0` and `max()` only ever raises it, so it can never be negative. `return max_profit` is the whole ending.
    2. **Indentation.** In my handwritten draft the `for` loop sat outside the method, at class level. Python would not even reach it. The loop belongs inside `maxProfit`, indented under the `def`.
    3. `float("inf")` works, but `min_value = prices[0]` is the other common way in. Either is fine, just say which you picked and why.

## Traces

**`[7,1,5,3,6,4]`**

| price | min_value | potential profit | max_profit |
|---|---|---|---|
| 7 | 7 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 5 | 1 | 4 | 4 |
| 3 | 1 | 2 | 4 |
| 6 | 1 | 5 | **5** |
| 4 | 1 | 3 | 5 |

**`[2,100,1]`**, the case that broke the first version

| price | min_value | potential profit | max_profit |
|---|---|---|---|
| 2 | 2 | 0 | 0 |
| 100 | 2 | 98 | **98** |
| 1 | 1 | 0 | 98 |

**`[7,6,4,3,1]`**, prices only fall

| price | min_value | potential profit | max_profit |
|---|---|---|---|
| 7 | 7 | 0 | 0 |
| 6 | 6 | 0 | 0 |
| 4 | 4 | 0 | 0 |
| 3 | 3 | 0 | 0 |
| 1 | 1 | 0 | **0** |

`max_profit` starts at `0` and never gets beaten, so a falling array returns `0` with no special casing at all.

---

## Next time

* When a problem forbids going backwards in time, think **running state**: running min, running max, running sum. That is usually the `O(n)` unlock.
* Two separate questions to ask in order. First *is it correct*, then *how much memory does it hold*. Fixing the logic and shrinking the space were two different edits here.
* **If you are building a list only to call `max()` or `min()` or `sum()` on it at the end, you do not need the list.** Keep a running value instead. `O(n)` space becomes `O(1)`.
* Test an idea against a small adversarial case before writing it. `[2, 100, 1]` would have killed the global minimum idea in fifteen seconds on paper.
* I guessed `log(x)` for the complexity. It is `O(n)`. `log` comes from repeatedly **halving** something, such as binary search. One pass over `n` items is linear.
