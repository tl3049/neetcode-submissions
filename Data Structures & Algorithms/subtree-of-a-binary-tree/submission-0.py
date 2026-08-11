# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        return self.isSametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    
    def isSametree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val is not q.val:
            return False
        else:
            return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)

        