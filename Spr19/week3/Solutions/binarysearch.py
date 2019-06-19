# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

import random
import time

# Our search algorithms returns index of the target element.
# If target not found, return -1
class Solution:
    def binarysearch(self, arr: list, target: int) -> int:
        left = 0
        right = len(arr)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid
            else:
                return mid
        return -1

    
    def sequentialsearch(self, arr: list, target: int) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i] == target:
                return i
        return -1


if __name__ == '__main__':
    random.seed(0)
    arr = sorted([random.randint(0, 1000000) for i in range(1000000)])
    target = 999723
    s = Solution()
    t0 = time.time()
    print(s.sequentialsearch(arr, target))
    t1 = time.time()
    seq_time = t1-t0
    print("Sequential Search took:", seq_time, "seconds.")
    t2 = time.time()
    print(s.binarysearch(arr, target))
    t3 = time.time()
    bin_time = t3-t2
    print("Binary Search took:", bin_time, "seconds.")
    print()
    print("Binary Search with 1,000,000 sorted elements is", seq_time/bin_time, "times faster")