# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter at a node = left depth + right depth

        # im thinking to go through each node in the tree 
        # and calculate the diameter
        # we can just do a dfs and calculate the diameter at each node
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            res = max(res, (left_depth + right_depth))
            return 1 + max(left_depth, right_depth)
        dfs(root)
        return res