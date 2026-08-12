# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # # path = []
        # def dfs(node, cur_val):
        #     if not node:
        #         return False
        #     path.append(node.val)
        #     val = cur_val + node.val
        #     if not node.left and not node.right:
        #         if val == targetSum:
        #             return True
        #         else:
        #             # path.pop()
        #             return False
        #     if dfs(node.left, val):
        #         return True
        #     if dfs(node.right, val):
        #         return True
        #     path.pop()
        #     return False
        # res = dfs(root, 0)
        # # print(path)
        # return res

        self.res = False
        def dfs(node, cur_val):
            if not node:
                return
            val = cur_val + node.val
            if not node.left and not node.right:
                if val == targetSum:
                    self.res = True 
                return
            if not self.res:
                dfs(node.left, val)
            if not self.res:
                dfs(node.right, val)
            return
        dfs(root, 0)
        return self.res