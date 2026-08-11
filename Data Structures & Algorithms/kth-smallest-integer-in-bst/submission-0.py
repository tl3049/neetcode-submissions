# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: 
            return False
        stack = [root]
        visited = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        visited = sorted(visited)
        return visited[k - 1]
        