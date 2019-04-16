# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from utils.TreeNode import TreeNode
from utils.BST import *
from utils.Stack import Stack

class Solution:
    def zigzag_level(self, root):
        if root is None:
            return

        curLevel = Stack()
        nextLevel = Stack()

        curLevel.push(root)
        ltr = True # left to right for level 1
        while not curLevel.isEmpty():
            temp = curLevel.pop()
            print(temp.val, end=" ")

            if ltr: # left to right
                if temp.left:
                    nextLevel.push(temp.left)
                if temp.right:
                    nextLevel.push(temp.right)
            else:   # right to left
                if temp.right:
                    nextLevel.push(temp.right)
                if temp.left:
                    nextLevel.push(temp.left)

            if curLevel.isEmpty():
                ltr = not ltr
                curLevel, nextLevel = nextLevel, curLevel
        print()

        

if __name__ == '__main__':
    tree = [1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], [7, None, None]]]
    root = list_to_tree(tree)
    # print_BST(root)
    s = Solution()
    s.zigzag_level(root)
    # Should print 1 3 2 4 5 6 7