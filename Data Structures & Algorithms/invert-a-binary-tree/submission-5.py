# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # to invert a binary tree, we need to swap the l and r children
        # of each node

        # recurse for sure

        if not root: # base case
            return
        # now we need to swap the actual children of the root node
        tmp = root.left
        root.left = root.right
        root.right = tmp
        # now we have swapped the children of this root node
        # recurse on its children
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        