# ------------------------------
# Standard Python DSA Template
# ------------------------------

import sys
import math
from collections import defaultdict, Counter, deque
from typing import List, Optional

# Fast input (useful for contests, not needed for Leetcode usually)
input = sys.stdin.readline

# Example: Solution class for Leetcode
class Solution:
    def exampleFunction(self, nums: List[int]) -> int:
        # Your logic goes here
        return sum(nums)

# ------------------------------
# Utility Functions
# ------------------------------

# GCD & LCM
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

# Prefix Sum
def prefix_sum(arr: List[int]) -> List[int]:
    ps = [0]
    for num in arr:
        ps.append(ps[-1] + num)
    return ps

# Sliding Window Max (template for variable window)
def sliding_window(arr: List[int], k: int) -> int:
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Binary Search Template
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ------------------------------
# Driver Code (local testing only)
# ------------------------------
if __name__ == "__main__":
    # Example test
    nums = [1, 2, 3, 4, 5]
    print("Prefix sum:", prefix_sum(nums))
    print("Sliding window (k=3):", sliding_window(nums, 3))
    print("Binary search (target=4):", binary_search(nums, 4))
