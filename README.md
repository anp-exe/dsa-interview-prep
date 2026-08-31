# dsa-interview-prep

LeetCode worked solutions for Google STEP interview prep, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

**Live site:** https://anp-exe.github.io/dsa-interview-prep/

Every problem follows the same four steps:

1. **Plan** the approach in English, including edge cases
2. **Pseudocode** the shape before touching syntax
3. **First attempt**, brute force or broken, with its complexity stated
4. **Optimise**, with the one reframing that removed the bottleneck


## Sections

| Section | Status |
|---|---|
| Easy | 3 written up |
| Medium | planned, see `docs/medium/index.md` |
| Hard | planned, see `docs/hard/index.md` |
| Complexity Cheat Sheet | Big O, pattern picker, Python gotchas |
| Problem Template | copy this to start a new write up |

## Running locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000`.

## Deploying

Deployment runs through **GitHub Actions**, not a `gh-pages` branch.

One time setup: repo **Settings → Pages → Build and deployment → Source → GitHub Actions**.

After that, every push to `main` runs `.github/workflows/deploy.yml`, which builds with `mkdocs build --strict` and publishes the result straight to Pages. No extra branch, and a failed build blocks the deploy instead of shipping a broken site.

## Checking the solutions

`verify_solutions.py` runs every solution on the site against the LeetCode examples plus edge cases, cross checks the optimised versions against brute force on random inputs, and proves the counterexamples quoted on the pages are real.

```bash
python3 verify_solutions.py
```

## Adding a problem

1. Copy the raw markdown from `docs/template.md` into a new file, for example `docs/medium/3sum.md`
2. Fill in the four steps
3. Add the page to `nav` in `mkdocs.yml`
4. Commit and push

## Structure

```text
mkdocs.yml                     site config, nav, theme
requirements.txt
verify_solutions.py            runs and checks every solution
.github/workflows/deploy.yml   builds and publishes on push to main
docs/
  index.md                     home, method, progress
  cheatsheet.md                Big O and pattern reference
  template.md                  starting point for a new problem
  assets/                      logo and favicon
  javascripts/wordmark.js      paints the anna wordmark
  stylesheets/extra.css        the four colour theme and custom boxes
  easy/                        Two Sum, Palindrome Number, Best Time to Buy and Sell Stock
  medium/
  hard/
```

## Colours and type

Four colour palette: `#4285F4` blue, `#EA4335` red, `#FBBC04` yellow, `#34A853` green. Body type is Questrial, the closest free stand in for Google's Product Sans. The mark is an original four arc design, not any company's trademark.

## Licence

MIT, see `LICENSE`.
