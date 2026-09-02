# Problem Template

Copy this into a new file under `docs/easy/`, `docs/medium/` or `docs/hard/`, then add it to the `nav` in `mkdocs.yml`.

---

## The raw markdown

````text
# Problem Name

<span class="pill medium">Medium</span> <span class="pill done">Solved</span> <span class="pill time">22 mins</span> <span class="pill">Sliding window</span>

[Open on LeetCode :material-open-in-new:](https://leetcode.com/problems/slug/){ .md-button }

---

## The question

One or two lines restating it, then the examples.

=== "Example 1"

    ```text
    Input:  ...
    Output: ...
    ```

**Constraints**

* ...

---

<div class="step-row">
  <div class="step-chip s1">1 · Plan<small>say it in English</small></div>
  <div class="step-chip s2">2 · Pseudocode<small>shape before syntax</small></div>
  <div class="step-chip s3">3 · First attempt<small>get it working</small></div>
  <div class="step-chip s4">4 · Optimise<small>then get it fast</small></div>
</div>

## 1 · Plan

!!! plan "What is actually being asked"

    Restate it. What is returned, values or indices? What are the edge cases?
    What is the obvious slow approach and what does it cost?

## 2 · Pseudocode

!!! pseudo "Shape"

    ```text
    ...
    ```

## 3 · First attempt

!!! attempt "What I wrote first"

    ```python
    ...
    ```

    Passed / failed on N of M. Time `O(?)`, space `O(?)`.
    If it failed, write the exact input that broke it and why.

## 4 · Optimise

!!! insight "The one idea to remember"

    One sentence. The reframing that removes the nested loop.

!!! optimise "Final solution"

    ```python
    ...
    ```

    | | Time | Space |
    |---|---|---|
    | First attempt | `O(?)` | `O(?)` |
    | Optimised | `O(?)` | `O(?)` |

!!! gotcha "Mistakes to not repeat"

    ...

---

## Next time

* ...
````

---

## The boxes available

| Write this | Get this |
|---|---|
| `!!! plan "Title"` | blue, for the plan |
| `!!! pseudo "Title"` | yellow, for pseudocode |
| `!!! attempt "Title"` | red, for the first or failed attempt |
| `!!! optimise "Title"` | green, for the final solution |
| `!!! insight "Title"` | purple, for the one idea worth remembering |
| `!!! gotcha "Title"` | orange, for mistakes to not repeat |
| `??? plan "Title"` | any of the above, collapsed by default |

!!! plan "This is a plan box"

    Blue. Use it for restating the question and listing edge cases.

!!! pseudo "This is a pseudocode box"

    Yellow. Use it for the shape of the algorithm before real syntax.

!!! attempt "This is an attempt box"

    Red. Use it for the version that was slow or broken, and say why.

!!! optimise "This is an optimise box"

    Green. Use it for the final solution and its complexity table.

!!! insight "This is an insight box"

    Purple. One sentence, the reframing that made it click.

!!! gotcha "This is a gotcha box"

    Orange. The mistake, and the fix.

---

## The pills

| Write this | Get this |
|---|---|
| `<span class="pill easy">Easy</span>` | <span class="pill easy">Easy</span> |
| `<span class="pill medium">Medium</span>` | <span class="pill medium">Medium</span> |
| `<span class="pill hard">Hard</span>` | <span class="pill hard">Hard</span> |
| `<span class="pill done">Solved</span>` | <span class="pill done">Solved</span> |
| `<span class="pill time">18 mins</span>` | <span class="pill time">18 mins</span> |
| `<span class="pill">Any label</span>` | <span class="pill">Any label</span> |

---

## Running it locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open `http://127.0.0.1:8000`. It live reloads on save.

Push to `main` and the GitHub Action rebuilds and publishes the site automatically.
