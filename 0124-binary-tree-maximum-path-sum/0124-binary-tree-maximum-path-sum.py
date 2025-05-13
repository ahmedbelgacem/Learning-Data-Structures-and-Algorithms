class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float("-inf")
        def recValue(root: Optional[TreeNode]) -> int:
            nonlocal max_val
            if not root:
                return 0
            l = max(recValue(root.left), 0)
            r = max(recValue(root.right), 0)
            max_val = max(root.val + l + r, max_val)
            return root.val + max(l, r)
        recValue(root)
        return max_val