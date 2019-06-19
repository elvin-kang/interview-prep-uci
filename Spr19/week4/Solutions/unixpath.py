# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from utils.Stack import Stack

class Solution:
    def unixpath(self, path: str) -> str:
        pathlist = path.split("/")
        stack = Stack()
        for p in pathlist:
            if p != "." and p != "..":
                stack.push(p)
            if p == "..":
                stack.pop()
        return "/".join(stack.toList())

if __name__ == '__main__':
    s = Solution()
    print(s.unixpath("/usr/bin/../src/./test/main/.././"))