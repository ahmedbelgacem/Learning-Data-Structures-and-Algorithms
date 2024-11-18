# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def queue(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root]
        else:
            return self.queue(root.right) + [root] + self.queue(root.left)
            
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_list = self.queue(root)
        last_value = 0
        for node in node_list:
            node.val += last_value
            last_value = node.val
        return root
