# Longest Common Prefix

<span class="pill easy">Easy</span> <span class="pill done">Solved</span> <span class="pill">String</span> <span class="pill">Vertical scan</span>

[Open on LeetCode :material-open-in-new:](https://leetcode.com/problems/longest-common-prefix/){ .md-button }

---

## The question

Find the longest common prefix string amongst an array of strings. If there is no common prefix, return `""`.

=== "Example 1"

    ```text
    Input:  strs = ["flower","flow","flight"]
    Output: "fl"
    ```

=== "Example 2"

    ```text
    Input:  strs = ["dog","racecar","car"]
    Output: ""
    No common prefix among the input strings.
    ```

**Constraints**

* `1 <= strs.length <= 200`
* `strs[i]` consists of only lowercase English letters if it is non-empty

---

<div class="step-row">
  <div class="step-chip s1">1 · Plan<small>say it in English</small></div>
  <div class="step-chip s2">2 · Pseudocode<small>shape before syntax</small></div>
  <div class="step-chip s3">3 · Working code<small>first try, passes</small></div>
  <div class="step-chip s4">4 · Tidy up<small>hoisting the min</small></div>
</div>

## 1 · Plan

!!! plan "What is actually being asked"

    Find the largest matching **start** of every string in the list. Nothing in common means return `""`.

    The input arrives as a list of words called `strs`.

    The approach: go through the words one letter at a time. Ask whether the letter at index 0 of word one equals index 0 of word two, word three, and so on. Then index 1, and so on.

    Care needed on one point: add each matching letter to the result **once**, not once per word. Otherwise the prefix comes out as gibberish.

    Stop conditions:

    * a mismatch at some column, so return what has been built so far
    * running out of letters, which happens when the **shortest** word is exhausted

!!! insight "The one idea to remember"

    Scan **columns, not rows**. Compare the character at index `i` across every word before moving to index `i + 1`. This is "vertical scanning", and it stops the moment a column disagrees, so a short common prefix is found fast even when the strings are long.

!!! note "Knowledge gap flagged for later"

    The LeetCode tags mention **Trie**, which is unfamiliar. Plan: brute force this first, then close the gap through the editorial and research and write up what a Trie actually is. Notes on that are at the bottom of this page.

## 2 · Pseudocode

!!! pseudo "Shape"

    ```text
    result = ""
    i = 0

    while i is still inside the shortest word
        letter = the letter at index i of the first word
        if every other word has that same letter at index i
            add letter to result
            i += 1
        else
            return result

    return result
    ```

??? note "Syntax worked out along the way"

    **First letter of the first word**

    ```python
    first_letter = strs[0][0]
    ```

    **Does every other word match it at that index**

    ```python
    if all(w[0] == first_letter for w in strs[1:]):
        print("all match")
    ```

    **Building the prefix up**

    ```python
    result = ""
    result += first_letter
    ```

    It does not have to be a list. A string uses less memory here and is what gets returned anyway.

## 3 · Working code

!!! optimise "Passes first try"

    ```python
    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            result = ""
            i = 0  # this will be the letter index

            while i < min([len(s) for s in strs]):
                letter = strs[0][i]
                if all(w[i] == letter for w in strs[1:]):
                    result += letter
                    i += 1
                else:
                    return result

            return result
    ```

    Checked against the examples, the edge cases and 4000 random arrays cross checked against a brute force. All correct.

!!! plan "Why `i < min(...)` is the right bound"

    The shortest word runs out of letters first, and once it is out there is nothing left to compare against.

    `["flower", "flow"]`:

    ```text
    i = 0   'f' vs 'f'
    i = 1   'l' vs 'l'
    i = 2   'o' vs 'o'
    i = 3   'w' vs 'w'
    i = 4   'e' vs  ???   <- "flow" has no letter 4
    ```

    Indexing past the end of a string is an `IndexError`, so the bound is doing real work, not just tidiness.

??? note "Two edge cases this handles without any special casing"

    **A single word**, `["abc"]`. Then `strs[1:]` is empty, and `all()` of an empty sequence is `True`. So every column passes and the whole word comes back as the prefix. Correct, and free.

    **An empty string in the list**, `["", "a"]`. Then the shortest length is `0`, the loop never runs, and `""` comes back. Also correct, also free.

    The one case that would break is an **empty list**, because `min()` of an empty sequence raises `ValueError`. The constraint `1 <= strs.length` rules it out, so no guard is needed here, but it is the first thing to ask about if the constraint were missing.

## 4 · One thing to tidy

!!! plan "Hoisting the `min` out of the loop"

    The `min` sits in the `while` condition, so it is re-evaluated **every single iteration**, and each time it builds a brand new list of every word length.

    On a `["a"*2000 + "x", ...]` style input with three words, the `min([...])` expression runs **2001 times**. It only needs to run once, because the lengths never change.

    ```python
    min_len = min(len(s) for s in strs)   # once, before the loop
    while i < min_len:
        ...
    ```

    Two changes there:

    * **Hoisting it out of the loop** removes 2000 redundant scans.
    * **`min(len(s) for s in strs)`** with a generator instead of `min([...])` with a list comprehension never builds the list at all.

    The second one matters for the space claim. The editorial says vertical scanning is `O(1)` space, but a list comprehension inside the loop holds a list of `n` lengths at a time, which is `O(n)`. With the generator it really is `O(1)`.

    Big O for time is unchanged either way, since both are bounded by `O(n · minLen)`. It is the constant factor and the space claim that improve.

!!! optimise "Tidied version"

    ```python
    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            min_len = min(len(s) for s in strs)
            i = 0

            while i < min_len:
                letter = strs[0][i]
                if all(w[i] == letter for w in strs[1:]):
                    i += 1
                else:
                    break

            return strs[0][:i]
    ```

    `strs[0][:i]` at the end replaces building `result` character by character. Same output, and it sidesteps the `s += ...` in a loop entry from the [cheat sheet](../cheatsheet.md).

## 5 · Complexity

!!! optimise "`O(S)` time, `O(1)` space"

    **Time is `O(S)`**, where `S` is the total number of characters across all strings. In the worst case there are `n` equal strings of length `m`, and the algorithm performs `S = m · n` character comparisons.

    The worst case matches horizontal scanning, but the **best** case is much better: at most `n · minLen` comparisons, and it exits at the first disagreeing column. A list like `["dog","racecar","car"]` is settled after one column.

    **Space is `O(1)`** once the list comprehension is gone. Only an index and a length are held. The returned prefix is the output, not extra working space.

---

## Alternatives

??? note "The lexicographic trick: only compare two strings"

    The common prefix of the whole list is the same as the common prefix of the **lexicographically smallest** and **largest** strings in it. Everything in between shares at least that much.

    ```python
    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            lo, hi = min(strs), max(strs)
            for i, ch in enumerate(lo):
                if i == len(hi) or hi[i] != ch:
                    return lo[:i]
            return lo
    ```

    Verified identical to the vertical scan on 4000 random arrays. `min(strs)` and `max(strs)` compare strings, not lengths, which is the part that makes it work.

??? note "What a Trie is, and why it is not the answer here"

    A **trie** (prefix tree) stores a set of words as a tree where each edge is a character and each path from the root spells a prefix. Words sharing a start share a branch.

    ```text
    root
     └── f
         └── l
             ├── o ── w ── e ── r     "flower"
             │        └── (end)       "flow"
             └── i ── g ── h ── t     "flight"
    ```

    The longest common prefix is then: walk down from the root while there is exactly **one** child and no word ends there. Above, `f` then `l`, then the branch splits, so the answer is `fl`.

    **It is not better for this problem.** Building the trie means inserting every character of every word, which is `O(S)`, the same as the vertical scan already costs, and then the tree itself is `O(S)` memory instead of `O(1)`.

    Where a trie earns its keep is **many prefix queries against one fixed set of words**: autocomplete, spell check, "how many stored words start with `pre`". Build once, then each query costs only the length of the query. One single query, as here, does not repay the build.

---

## Next time

* **Scan columns, not rows**, when every item has to agree at the same position.
* Anything inside a `while` condition runs on **every** iteration. Values that cannot change belong above the loop.
* `min(x for x in ...)` builds nothing. `min([x for x in ...])` builds a whole list first. Same answer, different space.
* `all()` of an empty sequence is `True`, which quietly handles the single-item case.
* A tag naming an unfamiliar structure is a knowledge gap to close **after** getting something working, not a reason to stall before starting.
