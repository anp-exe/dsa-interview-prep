"""Sanity check every solution on this site against the LeetCode examples plus edge cases."""
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
    min_price = float("inf")
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > best:
            best = price - min_price
    return best


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
    check("running min %s" % prices, max_profit(prices), want)
    check("brute       %s" % prices, max_profit_brute(prices), want)

check("broken version on [2,100,1] returns 0 as claimed", max_profit_broken([2, 100, 1]), 0)

random.seed(7)
bad = []
for _ in range(3000):
    p = [random.randint(0, 40) for _ in range(random.randint(1, 12))]
    if max_profit(p) != max_profit_brute(p):
        bad.append(p)
check("running min matches brute force on 3000 random arrays", bad, [])

print()
if fails:
    print("\n".join(fails))
    raise SystemExit(1)
print("ALL CHECKS PASSED")
