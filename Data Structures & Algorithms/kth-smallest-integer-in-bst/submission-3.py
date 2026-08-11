# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ##Recursive
        res = None

        def inorder(node):
            nonlocal k, res 
            if not node or res is not None:
                return
            inorder(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            inorder(node.right)

        inorder(root)
        return res
        
        
        
        ## DFS in order iterative
        # if not root: 
        #     return False
        # stack = []
        # cur = root
        # i = 0
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     node = stack.pop()
        #     i += 1
        #     if i == k:
        #         return node.val
        #     cur = node.right  
        ## Brute force
        # stack = [root]
        # visited = []
        # while stack:
        #     node = stack.pop()
        #     if node not in visited:
        #         visited.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # visited = sorted(visited)
        # return visited[k - 1]
        