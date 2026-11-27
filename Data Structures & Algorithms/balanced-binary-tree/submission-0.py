# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced = True

        def depth(node):
            if not node :
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # print(node.val, left_depth, right_depth, abs(left_depth - right_depth))
            if abs(left_depth - right_depth) > 1:
                self.isbalanced = False
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.isbalanced