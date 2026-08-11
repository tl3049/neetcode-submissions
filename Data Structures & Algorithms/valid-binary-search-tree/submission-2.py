# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))
        # if not root:
        #     return False
        # p, q = root.left, root.right 
        # if not p or not q:
        #     if not p and not q:
        #         return True
        #     if not p and q:
        #         if q.val > root.val:
        #             return True
        #         else:
        #             return False
        #     if p and not q:
        #         if p.val < root.val:
        #             return True
        #         else: 
        #             return False
        # if p.val < root.val and q.val > root.val:
        #     return self.isValidBST(p) and self.isValidBST(q)
        # else:
        #     return False
    def valid(self, node, l_res, r_res):
        if not node:
            return True
        if not(l_res < node.val and node.val < r_res): 
            return False
        else:
            return self.valid(node.left, l_res, node.val) and self.valid(node.right, node.val, r_res)
        


            