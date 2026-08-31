# Complexity Cheat Sheet

Everything worth having in your head before an interview, on one page.

---

## Big O, read off the shape of the code

| You see | Complexity | Name | Feels like |
|---|---|---|---|
| Arithmetic, a dict lookup, a list index | `O(1)` | constant | instant |
| Repeatedly halving the input | `O(log n)` | logarithmic | binary search |
| One loop over `n` | `O(n)` | linear | one pass |
| A sort, or a loop that does a `log n` job each time | `O(n log n)` | linearithmic | `sorted()` |
| Two nested loops over `n` | `O(n²)` | quadratic | every pair |
| Every subset | `O(2ⁿ)` | exponential | avoid |
| Every ordering | `O(n!)` | factorial | really avoid |

!!! insight "The rule that generates all of these"

    `log` appears when something **halves**. `n` appears when you **touch each item once**. `n²` appears when you **pair each item with each item**. Ask which of the three the code is doing and you have the answer without memorising anything.

!!! gotcha "Complexity mistakes that are easy to make"

    * A loop nested inside a loop is `n²` **even when the inner loop looks short**, unless it is bounded by a constant.
    * `min()`, `max()`, `sum()`, `in list`, `list.index()` and slicing are each a **full pass**. Four of them in a row is four passes, still `O(n)`, but if the problem wants one pass you have not delivered it.
    * `x in some_list` is `O(n)`. `x in some_set` and `x in some_dict` are `O(1)`. This one distinction fixes an enormous number of timeouts.
    * Building a string with `s += ...` inside a loop is `O(n²)` in Python. Append to a list and `"".join()` it at the end.
    * Recursion costs stack space. `O(1)` extra space means no recursion either.

---

## Python operation costs

| Operation | Cost |
|---|---|
| `d[key]`, `key in d`, `d[key] = v` | `O(1)` average |
| `s.add(x)`, `x in s` (set) | `O(1)` average |
| `lst[i]`, `lst.append(x)`, `lst.pop()` | `O(1)` |
| `lst.pop(0)`, `lst.insert(0, x)` | `O(n)`, shifts everything |
| `x in lst`, `lst.index(x)`, `lst.count(x)` | `O(n)` |
| `lst[a:b]` | `O(b - a)`, it copies |
| `sorted(lst)`, `lst.sort()` | `O(n log n)` |
| `min(lst)`, `max(lst)`, `sum(lst)` | `O(n)` |
| `heapq.heappush` / `heappop` | `O(log n)` |
| `collections.deque.popleft()` | `O(1)`, use this instead of `lst.pop(0)` |

---

## Pattern picker

Read the problem, match the phrase, reach for the tool.

| The problem says | Reach for | Typical cost |
|---|---|---|
| "find two things that sum to", "have I seen this", "find the duplicate" | **hash map or set** | `O(n)` |
| "sorted array", "find the position of" | **binary search** | `O(log n)` |
| "pair from a sorted array", "from both ends", "reverse in place" | **two pointers** | `O(n)` |
| "longest / shortest substring or subarray with a property" | **sliding window** | `O(n)` |
| "maximum so far", "cannot go backwards in time", "best up to here" | **running state, greedy** | `O(n)` |
| "top k", "k largest", "merge k sorted" | **heap** | `O(n log k)` |
| "matching brackets", "undo", "most recent" | **stack** | `O(n)` |
| "shortest path in unweighted graph", "level by level" | **BFS with a deque** | `O(V + E)` |
| "all paths", "connected components", "flood fill" | **DFS or recursion** | `O(V + E)` |
| "count the ways", "min cost to reach", "overlapping subproblems" | **dynamic programming** | usually `O(n)` or `O(n²)` |
| "prefix", "autocomplete", "shared start of words" | **trie** | `O(word length)` |
| "overlapping ranges", "meeting rooms" | **sort by start, then sweep** | `O(n log n)` |

---

## The four patterns already met

!!! plan "Hash map complement, from Two Sum"

    ```python
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    ```

    Store as you go, check **before** you store. Anything in the map is guaranteed to be an earlier element.

!!! plan "Digit peeling, from Palindrome Number"

    ```python
    while x > 0:
        digit = x % 10     # last digit
        x //= 10           # drop it
    ```

    The pure arithmetic answer to anything that says "without converting to a string".

!!! plan "Running state, from Best Time to Buy and Sell Stock"

    ```python
    best_so_far = float("inf")
    answer = 0
    for item in items:
        best_so_far = min(best_so_far, item)
        answer = max(answer, item - best_so_far)
    ```

    One pass. The "cannot use a future value" rule enforces itself, because the running state only ever holds the past.

!!! plan "Two pointers, coming up in Medium"

    ```python
    left, right = 0, len(arr) - 1
    while left < right:
        # decide which end to move, based on the condition
        ...
    ```

    Turns an `O(n²)` pair search into `O(n)` when the array is sorted.

---

## Python gotchas that keep costing marks

| Mistake | Fix |
|---|---|
| `true` / `false` | `True` / `False`, capitalised |
| `if cond: return True else: return False` | `return cond` |
| Naming a variable `reversed`, `list`, `dict`, `sum`, `max`, `input` | shadows a built in, pick another name |
| `d[[1, 2]]` | lists are unhashable, keys must be tuples. Values can be lists |
| Expecting `defaultdict` to pre create keys | it creates a default **on first access** of a missing key |
| `for x in lst: lst.remove(x)` | never mutate a list while iterating it, build a new one |
| `def f(x, acc=[])` | mutable default argument, use `acc=None` then `acc = acc or []` |
| Guard clause indented so the rest of the function sits inside it | the guard returns, the rest continues at the same level |
| Integer division with `/` | `/` gives a float, use `//` for integer division |

---

## Interview script

The four steps, in the words you would actually say out loud.

1. **Restate it.** "So I am given X, and I need to return Y. Can I confirm that duplicates are allowed and the input is never empty?"
2. **Name the brute force and its cost.** "The obvious approach is every pair, which is `O(n²)`. Let me get that down and then improve it."
3. **Walk a small example by hand.** This is where the optimisation usually appears, and it proves the code before running it.
4. **State the final complexity and the trade.** "`O(n)` time and `O(n)` space. I am buying time with memory. If space were tight I would sort first and use two pointers instead, for `O(n log n)` time and `O(1)` extra space."
5. **Say the edge cases.** Empty input, one element, all identical, all negative, already sorted, reverse sorted.

!!! insight "The thing being graded"

    Communication and process, not recall. A candidate who narrates a wrong idea, spots the counterexample themselves and fixes it beats a candidate who silently types the optimal answer.
