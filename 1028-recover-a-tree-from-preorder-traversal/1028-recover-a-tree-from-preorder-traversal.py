# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if "-" not in traversal:
            return TreeNode(int(traversal), None, None)
        else:
            val = ""
            i = 0
            while traversal[i] != "-":
                val += traversal[i]
                i += 1
            val = int(val)
            dash = ""
            while traversal[i] == "-":
                dash += traversal[i]
                i += 1
            pattern = rf'(?<!-){dash}(?!-)'
            result = re.split(pattern, traversal[i:])
            left = self.recoverFromPreorder(result[0])
            right = None
            if len(result) == 2:
                right = self.recoverFromPreorder(result[1])
            return TreeNode(val, left, right)