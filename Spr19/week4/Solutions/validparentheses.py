# Path setup - do not modify
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
sys.path.append("../../")

from utils.Stack import Stack

# leetcode #20
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = Stack()
        for char in s:
            if char in mapping:
                top = stack.pop() if len(stack) != 0 else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.push(char)
        return len(stack) == 0

# cpp solution

# class Solution {
# public:
#     bool isValid(string s) {
#         stack<char> stack;
#         for(auto c : s) {
#             if(c == '(' || c == '{' || c == '[') {
#                 stack.push(c);
#             }
#             else if(!stack.empty() &&
#                     ((c == ')' && stack.top() == '(')
#                      || (c == '}' && stack.top() == '{')
#                      || (c == ']' && stack.top() == '['))) {
#                 stack.pop();
#             }
#             else {
#                 return false;
#             }
#         }
#         return stack.empty();
#     }
# };