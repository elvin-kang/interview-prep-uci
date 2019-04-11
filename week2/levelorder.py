# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from utils.TreeNode import TreeNode
from utils.BST import *
from utils.Queue import Queue
from utils.Stack import Stack

class Solution:
    def print_level(self, root):
        pass

if __name__ == '__main__':
    tree = [1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], [7, None, None]]]
    root = list_to_tree(tree)
    print_BST(root)
    s = Solution()
    print(s.print_level(root))
    # Should print out: 1 3 2 4 5 6 7