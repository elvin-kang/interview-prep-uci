# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

class Solution:
    def merge(self, l1, l2):
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

if __name__ == '__main__':
    s = Solution()
    print(s.merge([1, 5, 6, 9, 11], [2, 3, 7, 8, 18, 21]))