# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

class Solution:
    def mergesort(self, arr: list , begin: int, end: int) -> list:
        if len(arr) == 0 or begin > end:
            return list()
        
        if begin == end:
            return [arr[end]]
        
        left = self.mergesort(arr, begin, begin + (end - begin) // 2)
        right = self.mergesort(arr, begin + (end - begin) // 2 + 1, end)

        return self.merge(left, right)

    def merge(self, l1: list, l2: list):
        len1 = len(l1)
        len2 = len(l2)
        res = list()
        i = j = 0

        while i < len1 and j < len2:
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        
        # remaining elements for l1
        while i < len1:
            res.append(l1[i])
            i += 1
        
        # remaining elements for l2
        while j < len2:
            res.append(l2[j])
            j += 1

        return res

def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

if __name__ == '__main__':
    s = Solution()
    arr = [1, 31, 24, 9, 11, 2, 10, 7, 77, 18, 21]
    sorted_arr = s.mergesort(arr, 0, len(arr)-1)
    print(sorted_arr)
    print("pass" if is_sorted(sorted_arr) else "failed")