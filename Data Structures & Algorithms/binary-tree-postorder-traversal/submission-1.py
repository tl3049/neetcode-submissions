# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #ITERATIVE
        stack = [root]
        visit = [False]
        res = []
        while stack:
            cur, visited = stack.pop(), visit.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)
        return res

       
        # RECURSION
        # res = []
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     dfs(root.right)
        #     res.append(root.val)
        # dfs(root)
        # return res


