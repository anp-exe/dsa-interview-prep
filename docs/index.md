---
hide:
  - toc
---

<div class="hero" markdown>

<h1 class="wordmark-xl">Google <span class="wm-b">S</span><span class="wm-r">T</span><span class="wm-y">E</span><span class="wm-g">P</span> Interview Prep</h1>

<p class="subtitle">Documenting my journey of learning DSA and LeetCode from scratch. <strong>0 to STEP interview.</strong></p>

[:simple-leetcode: anp_exe on LeetCode](https://leetcode.com/u/anp_exe/){ .lc-link }

</div>

<div class="pullquote" markdown>

A lot of these easies become **hards** when you have to solve it with
`O(1)` space, time, in place, one pass, **cure cancer** during it, etc.

<span class="attrib">ssredotime, LeetCode discussion</span>

</div>

## The method

<div class="step-row">
  <div class="step-chip s1">1 · Plan<small>What is really being asked? What are the edge cases? Say it in English first.</small></div>
  <div class="step-chip s2">2 · Pseudocode<small>Get the shape down before fighting with syntax.</small></div>
  <div class="step-chip s3">3 · Brute force<small>Working beats clever. State the complexity out loud.</small></div>
  <div class="step-chip s4">4 · Optimise<small>Find the one idea that removes the nested loop.</small></div>
</div>

---

## Progress

**Easy** · 8 of 8 written up
<div class="bar"><span class="b-easy" style="width:100%"></span></div>

**Medium** · 0 written up
<div class="bar"><span class="b-medium" style="width:2%"></span></div>

**Hard** · 0 written up
<div class="bar"><span class="b-hard" style="width:2%"></span></div>

---

## Sections

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .g-green } **[Easy](easy/index.md)**

    ---

    Hash maps, digit arithmetic, running state. The patterns everything else is built on.

    <span class="pill easy">3 solved</span>

-   :material-numeric-2-circle:{ .lg .g-yellow } **[Medium](medium/index.md)**

    ---

    Two pointers, sliding window, binary search, intervals, graphs. The real interview range.

    <span class="pill medium">Up next</span>

-   :material-numeric-3-circle:{ .lg .g-red } **[Hard](hard/index.md)**

    ---

    Dynamic programming, heaps, tricky graph work. For later.

    <span class="pill hard">Not yet</span>

-   :material-lightning-bolt:{ .lg .g-blue } **[Cheat Sheet](cheatsheet.md)**

    ---

    Big O by shape, the pattern to reach for per problem type, and the Python mistakes that keep recurring.

    <span class="pill">Reference</span>

-   :material-cube-outline:{ .lg .g-green } **[OOP in Python](oop.md)**

    ---

    Classes, objects, `self`, and the four pillars. The vocabulary behind the tree in Climbing Stairs.

    <span class="pill">Reference</span>

</div>

---

## Solved so far

| Problem                                                                    | Difficulty                          | Pattern                 | Time       | Space  |
|----------------------------------------------------------------------------|-------------------------------------|-------------------------|------------|--------|
| [Two Sum](easy/two-sum.md)                                                 | <span class="pill easy">Easy</span> | Hash map complement     | `O(n)`     | `O(n)` |
| [Palindrome Number](easy/palindrome-number.md)                             | <span class="pill easy">Easy</span> | Digit arithmetic        | `O(log x)` | `O(1)` |
| [Best Time to Buy and Sell Stock](easy/best-time-to-buy-and-sell-stock.md) | <span class="pill easy">Easy</span> | Running minimum, greedy | `O(n)`     | `O(1)` |
| [Roman to Integer](easy/roman-to-integer.md) | <span class="pill easy">Easy</span> | Hash map with the exceptions in the table | `O(n)` | `O(1)` |
| [Longest Common Prefix](easy/longest-common-prefix.md) | <span class="pill easy">Easy</span> | Vertical scan, column by column | `O(S)` | `O(1)` |
| [Valid Parentheses](easy/valid-parentheses.md) | <span class="pill easy">Easy</span> | Stack, LIFO matching | `O(n)` | `O(n)` |
| [Climbing Stairs](easy/climbing-stairs.md) | <span class="pill easy">Easy</span> | Fibonacci recurrence, bottom up DP | `O(n)` | `O(1)` |
| [Merge Sorted Array](easy/merge-sorted-array.md) | <span class="pill easy">Easy</span> | Two pointers from the end, in place | `O(m+n)` | `O(1)` |

New problem? Start from the [template](template.md).

---

<div class="pullquote" markdown>

I fear not the man who has solved **1000 problems**,
but the man who has solved **1 problem 1000 times**.

</div>
