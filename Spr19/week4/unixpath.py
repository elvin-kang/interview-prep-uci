# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

# Which one do you need? Both?
# Comment out the module that you don't need if there's one.
from utils.Stack import Stack
from utils.Queue import Queue

class Solution:
    def unixpath(self, path: str) -> str:
        pass

if __name__ == '__main__':
    s = Solution()
    print(s.unixpath("/usr/bin/../src/./test/main/.././"))