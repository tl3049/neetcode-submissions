# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        #dfs max sum without split
        def dfs(node):
            if not node:
                return 0
            leftmax = max(dfs(node.left), 0)
            rightmax = max(dfs(node.right), 0)

            nonlocal res
            res = max(res, leftmax + rightmax + node.val)#update the total sum
            return node.val + max(leftmax, rightmax) #return the max sum without split
        dfs(root)

        return res 

