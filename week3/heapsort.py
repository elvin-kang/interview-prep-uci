# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from utils.PriorityQueue import PriorityQueue

class Solution:
    def heapsort(self, arr: list) -> list:
        pq = PriorityQueue(arr)
        print("heap:", pq._heap)
        res = list()
        while not pq.isEmpty():
            res.append(pq.poll())
        return res

def is_sorted(arr: list) -> bool:
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
    

if __name__ == '__main__':
    s = Solution()
    arr = [1, 31, 24, 9, 11, 2, 10, 7, 77, 18, 21]
    sorted_arr = s.heapsort(arr)
    print(sorted_arr)
    print()
    print("pass" if is_sorted(sorted_arr) else "failed")

    # make your own test case