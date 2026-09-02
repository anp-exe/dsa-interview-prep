"""Sanity check every solution on this site against the LeetCode examples plus edge cases."""
import itertools
import random
from typing import List


# ---------- Two Sum ----------
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


def two_sum_brute(nums: List[int], target: int) -> List[int]:
    i = 0
    for num in nums:
        j = 0
        for num2 in nums:
            if i == j:
                pass
            elif num + num2 == target:
                return [i, j]
            j = j + 1
        i = i + 1


# ---------- Palindrome Number ----------
def is_pal_str(x: int) -> bool:
    return str(x) == str(x)[::-1]


def is_pal_fast(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10
    return x == reverted or x == reverted // 10


# ---------- Best Time to Buy and Sell Stock ----------
def max_profit(prices: List[int]) -> int:
    """Final version on the page: running min + running max, O(1) space."""
    min_value = float("inf")
    max_profit_so_far = 0
    for price in prices:
        min_value = min(min_value, price)
        potential_profit = price - min_value
        max_profit_so_far = max(max_profit_so_far, potential_profit)
    return max_profit_so_far


def max_profit_list(prices: List[int]) -> int:
    """Intermediate version on the page: running min + a list of profits, O(n) space."""
    min_value = float("inf")
    profit = []
    for price in prices:
        min_value = min(min_value, price)
        profit.append(price - min_value)
    return max(profit)


def max_profit_broken(prices: List[int]) -> int:
    """The failed attempt, kept to prove the counterexample on the page is real."""
    min_value = min(prices)
    profit = []
    i = prices.index(min(prices))
    tail = prices[i:]
    for price in tail:
        if price - min_value >= 0:
            profit.append(price - min_value)
    max_num = max(profit)
    return max_num if max_num >= 0 else 0


def max_profit_brute(prices: List[int]) -> int:
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


fails = []


def check(label, got, want):
    if got != want:
        fails.append("FAIL %s: got %r, want %r" % (label, got, want))
    else:
        print("  ok  %s: %r" % (label, got))


print("Two Sum")
for nums, target, want in [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-3, 4, 3, 90], 0, [0, 2]),
    ([0, 4, 3, 0], 0, [0, 3]),
]:
    check("hashmap %s t=%s" % (nums, target), two_sum(nums, target), want)
    check("brute   %s t=%s" % (nums, target), sorted(two_sum_brute(nums, target)), sorted(want))

print("\nPalindrome Number")
for x, want in [
    (121, True), (-121, False), (10, False), (0, True), (1, True),
    (1221, True), (12321, True), (1234321, True), (100, False),
    (11, True), (1000021, False), (-101, False),
]:
    check("string  x=%s" % x, is_pal_str(x), want)
    check("halfrev x=%s" % x, is_pal_fast(x), want)

mismatch = [n for n in range(-500, 20001) if is_pal_str(n) != is_pal_fast(n)]
check("palindrome methods agree over -500..20000", mismatch, [])

print("\nBest Time to Buy and Sell Stock")
for prices, want in [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1], 0),
    ([1, 2], 1),
    ([2, 1], 0),
    ([2, 100, 1], 98),
    ([3, 3, 3], 0),
    ([2, 4, 1], 2),
]:
    check("running min, O(1) space %s" % prices, max_profit(prices), want)
    check("running min, O(n) space %s" % prices, max_profit_list(prices), want)
    check("brute force             %s" % prices, max_profit_brute(prices), want)

check("broken version on [2,100,1] returns 0 as claimed", max_profit_broken([2, 100, 1]), 0)

random.seed(7)
bad = []
for _ in range(3000):
    p = [random.randint(0, 40) for _ in range(random.randint(1, 12))]
    b = max_profit_brute(p)
    if max_profit(p) != b or max_profit_list(p) != b:
        bad.append(p)
check("both running-min versions match brute force on 3000 random arrays", bad, [])

# the page claims price - min_value is never negative, so the old ">= 0" guard was dead code
negative_seen = []
for _ in range(3000):
    p = [random.randint(-50, 60) for _ in range(random.randint(1, 14))]
    mv = float("inf")
    for price in p:
        mv = min(mv, price)
        if price - mv < 0:
            negative_seen.append(p)
            break
check("potential_profit is never negative, as the page claims", negative_seen, [])


# ---------- Roman to Integer ----------
def roman_to_int(s: str) -> int:
    """The thirteen entry version on the page."""
    roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                  "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    num = 0
    i = 0
    while i < len(s):
        if s[i:i + 2] in roman_nums:
            num += roman_nums[s[i:i + 2]]
            i += 2
        else:
            num += roman_nums[s[i]]
            i += 1
    return num


def roman_to_int_lookahead(s: str) -> int:
    """The seven entry alternative on the page."""
    value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and value[s[i]] < value[s[i + 1]]:
            total -= value[s[i]]
        else:
            total += value[s[i]]
    return total


def int_to_roman(n: int) -> str:
    """Only used to generate test data."""
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
             (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = []
    for v, sym in table:
        while n >= v:
            out.append(sym)
            n -= v
    return "".join(out)


print("\nRoman to Integer")
for text, want in [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994), ("IV", 4), ("IX", 9),
                   ("XL", 40), ("XC", 90), ("CD", 400), ("CM", 900), ("I", 1),
                   ("MMMCMXCIX", 3999), ("MMXXIV", 2024)]:
    check("pairs     %s" % text, roman_to_int(text), want)
    check("lookahead %s" % text, roman_to_int_lookahead(text), want)

wrong = [n for n in range(1, 4000)
         if roman_to_int(int_to_roman(n)) != n or roman_to_int_lookahead(int_to_roman(n)) != n]
check("both versions on all 3999 valid numerals", wrong, [])


# ---------- Longest Common Prefix ----------
def longest_common_prefix(strs):
    """The version on the page, exactly as written."""
    result = ""
    i = 0
    while i < min([len(s) for s in strs]):
        letter = strs[0][i]
        if all(w[i] == letter for w in strs[1:]):
            result += letter
            i += 1
        else:
            return result
    return result


def longest_common_prefix_tidy(strs):
    """Same logic with the min hoisted out of the loop and a slice at the end."""
    min_len = min(len(s) for s in strs)
    i = 0
    while i < min_len:
        letter = strs[0][i]
        if all(w[i] == letter for w in strs[1:]):
            i += 1
        else:
            break
    return strs[0][:i]


def longest_common_prefix_minmax(strs):
    """The lexicographic alternative on the page."""
    lo, hi = min(strs), max(strs)
    for i, ch in enumerate(lo):
        if i == len(hi) or hi[i] != ch:
            return lo[:i]
    return lo


def lcp_brute(strs):
    """Only used as the reference to check the others against."""
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print("\nLongest Common Prefix")
for arr, want in [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""),
                  (["a"], "a"), (["", ""], ""), (["", "a"], ""), (["abc", "abc"], "abc"),
                  (["ab", "abc"], "ab"), (["reflower", "flow", "flight"], "")]:
    check("vertical %s" % arr, longest_common_prefix(arr), want)
    check("tidied   %s" % arr, longest_common_prefix_tidy(arr), want)
    check("min/max  %s" % arr, longest_common_prefix_minmax(arr), want)

random.seed(3)
mismatch = []
for _ in range(4000):
    base = "".join(random.choice("ab") for _ in range(random.randint(0, 6)))
    arr = [base + "".join(random.choice("ab") for _ in range(random.randint(0, 4)))
           for _ in range(random.randint(1, 5))]
    want = lcp_brute(arr)
    if (longest_common_prefix(arr) != want
            or longest_common_prefix_tidy(arr) != want
            or longest_common_prefix_minmax(arr) != want):
        mismatch.append(arr)
check("all three versions match brute force on 4000 random arrays", mismatch, [])


# ---------- Valid Parentheses ----------
def is_valid(s: str) -> bool:
    """The final version on the page."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for bracket in s:
        if bracket in pairs:
            if not stack or stack.pop() != pairs[bracket]:
                return False
        else:
            stack.append(bracket)
    return not stack


def is_valid_chain(s: str) -> bool:
    """The elif-chain version, kept to prove the two agree."""
    stack = []
    for bracket in s:
        if bracket in ["{", "[", "("]:
            stack.append(bracket)
        elif bracket in ["}", "]", ")"]:
            if stack == []:
                return False
            elif stack[-1] == "{" and bracket == "}":
                stack.pop()
            elif stack[-1] == "(" and bracket == ")":
                stack.pop()
            elif stack[-1] == "[" and bracket == "]":
                stack.pop()
            else:
                return False
    return stack == []


def is_valid_naive(s: str) -> bool:
    """The first attempt, kept to measure how wrong presence-checking is."""
    if "(" in s and ")" not in s:
        return False
    elif "[" in s and "]" not in s:
        return False
    elif "{" in s and "}" not in s:
        return False
    else:
        return True


print("\nValid Parentheses")
for text, want in [("()", True), ("()[]{}", True), ("(]", False), ("([])", True),
                   ("([)]", False), ("", True), ("(", False), (")", False),
                   (")(", False), ("{[()]}", True), ("[{]}", False), ("((((", False)]:
    check("stack %r" % text, is_valid(text), want)
    check("chain %r" % text, is_valid_chain(text), want)

# exhaustive: every bracket string up to length 8
wrong_final = wrong_chain = wrong_naive = total = 0
for length in range(0, 9):
    for combo in itertools.product("()[]{}", repeat=length):
        text = "".join(combo)
        total += 1
        want = is_valid(text)
        if is_valid_chain(text) != want:
            wrong_chain += 1
        if is_valid_naive(text) != want:
            wrong_naive += 1
check("chain matches final on all %d bracket strings of length 0..8" % total, wrong_chain, 0)
print("       (the naive presence-check version is wrong on %d of them, %.0f%%)"
      % (wrong_naive, 100 * wrong_naive / total))

print()
if fails:
    print("\n".join(fails))
    raise SystemExit(1)
print("ALL CHECKS PASSED")
