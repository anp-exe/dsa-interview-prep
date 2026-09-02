# Two Sum

<span class="pill easy">Easy</span> <span class="pill done">Solved</span> <span class="pill time">13 mins</span> <span class="pill">Hash map</span>

[Open on LeetCode :material-open-in-new:](https://leetcode.com/problems/two-sum/){ .md-button }

---

## The question

Given an array of integers `nums` and an integer `target`, return **indices of the two numbers such that they add up to `target`**.

Each input has **exactly one solution**, and you may not use the same element twice. The answer can be returned in any order.

=== "Example 1"

    ```text
    Input:  nums = [2,7,11,15], target = 9
    Output: [0,1]
    Because nums[0] + nums[1] == 9
    ```

=== "Example 2"

    ```text
    Input:  nums = [3,2,4], target = 6
    Output: [1,2]
    ```

=== "Example 3"

    ```text
    Input:  nums = [3,3], target = 6
    Output: [0,1]
    ```

**Constraints**

* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* Only one valid answer exists.

**Follow up:** can you do better than `O(n²)` time?

---

<div class="step-row">
  <div class="step-chip s1">1 · Plan<small>say it in English</small></div>
  <div class="step-chip s2">2 · Pseudocode<small>shape before syntax</small></div>
  <div class="step-chip s3">3 · Brute force<small>get it working</small></div>
  <div class="step-chip s4">4 · Optimise<small>then get it fast</small></div>
</div>

## 1 · Plan

!!! plan "What is actually being asked"

    Find the two numbers that add to `target`, then return **their positions**, not the numbers themselves.

    Things to notice before writing anything:

    * Return **indices**. Easy to solve the wrong problem here.
    * The same element cannot be used twice, so `i != j`.
    * Exactly one solution exists, which means no tie breaking and no "return empty if nothing found" logic to worry about.
    * `[3,3]` is legal, so duplicate **values** are fine. Only duplicate **indices** are banned.

    The obvious approach is to try every pair. The follow up is telling me that a faster one exists, so I should expect to come back and improve it.

## 2 · Pseudocode

!!! pseudo "Brute force shape"

    ```text
    for each index i in nums
        for each index j in nums
            skip if i == j
            if nums[i] + nums[j] == target
                return [i, j]
    ```

    That is two nested loops, so `n × n` work. Fine as a first pass, but it will not survive the follow up.

## 3 · Brute force

!!! attempt "First working version"

    ```python
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            i = 0
            for num in nums:
                j = 0
                for num2 in nums:
                    if i == j:
                        continue
                    elif num + num2 == target:
                        return [i, j]
                    j = j + 1
                i = i + 1
    ```

    This passes. Time `O(n²)`, space `O(1)`.

!!! gotcha "Manual index counters are a trap"

    Tracking `i` and `j` by hand with `i = i + 1` works, but it is the single easiest place to introduce an off by one bug. Python provides this directly:

    ```python
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums):
            ...
    ```

    Same logic, one fewer thing to get wrong. Use `enumerate` whenever both the value and the position are needed.

## 4 · Optimise

!!! insight "The one idea to remember"

    Stop asking **"which two numbers add to target"**. Ask **"for the number I am looking at right now, have I already seen `target - num`?"**

    That turns a search over pairs into a single pass with a lookup, because a hash map answers "have I seen this" in `O(1)`.

!!! optimise "One pass hash map, `O(n)` time"

    ```python
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen = {}                          # value -> index it was found at
            for i, num in enumerate(nums):
                complement = target - num
                if complement in seen:
                    return [seen[complement], i]
                seen[num] = i
    ```

    **Why it is correct:** `seen` only ever contains numbers from indices **before** `i`, so any hit is guaranteed to be a different element. The "use each element once" rule is handled by the ordering, not by an `if i == j` check.

    **Why the store comes after the check:** for `nums = [3,3], target = 6`, at `i = 0` nothing is in `seen` yet, so `3` gets stored. At `i = 1` the complement `3` is found and `[0, 1]` is returned. Storing first would match a number against itself.

    | | Time | Space |
    |---|---|---|
    | Brute force | `O(n²)` | `O(1)` |
    | Hash map | `O(n)` | `O(n)` |

    That is the classic trade: time bought with memory.

---

## Concept notes

??? note "Array lookup vs hash map lookup"

    ```python
    # array: scan until it is found
    users = [("ana@x.com", 24), ("ben@x.com", 31)]
    for email, age in users:
        if email == "cleo@x.com":
            print(age)
            break
    # worst case checks every entry. O(n).
    ```

    ```python
    # hash map: jump straight there
    users = {"ana@x.com": 24, "ben@x.com": 31}
    print(users["cleo@x.com"])
    # one hop. O(1) average.
    ```

    In Python a hash map **is** a dictionary. The hashing happens behind the scenes, which is why `.index(x)` on a list is `O(n)` but `d[x]` on a dict is `O(1)`.

??? note "Nesting the two structures"

    ```python
    # dict whose values are lists
    teams = {"red": ["ana", "ben"], "blue": ["cleo"]}
    teams["red"].append("dev")

    # list of dicts, which is the shape of nearly every API response
    people = [{"name": "ana", "age": 24}, {"name": "ben", "age": 31}]
    for p in people:
        print(p["name"])
    ```

??? gotcha "Two things worth correcting from my first notes"

    **"You have to convert a list to a tuple."** Only when the list is being used as a **key**. Dict keys must be hashable and lists are not, so `d[[1,2]]` fails and `d[(1,2)]` works. Values can be lists quite happily: `{"red": ["ana"]}` is fine.

    **"A dict needs keys initialised, a defaultdict has them already initialised."** Not quite. A `defaultdict` does not pre create anything. It creates a default value **the moment a missing key is touched**, so `d["new"].append(1)` works instead of raising `KeyError`. Useful for grouping, not needed here.

---

## Next time

* Reach for a hash map the second a problem says "find a pair / find a duplicate / have I seen this before".
* Write the brute force, state its complexity out loud, then improve it. The progression is what gets marked, not a memorised answer.
* Use `enumerate` instead of hand rolled counters.
