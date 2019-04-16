# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

class Solution:
    def merge(self, l1, l2):
        pass

if __name__ == '__main__':
    s = Solution()
    print(s.merge([1, 5, 6, 9, 11], [2, 3, 7, 8, 18, 21]))

    # make your own test cases