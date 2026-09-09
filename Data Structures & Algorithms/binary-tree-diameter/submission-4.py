# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    m=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is not None:
                l = height(root.left)
                r = height(root.right)
                self.m = max(self.m, l+r)
                return max(l, r) +1
            else:
                return 0
        height(root)
        return self.m