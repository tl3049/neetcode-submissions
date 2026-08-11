# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # return depth
    #BFS+queue    
        # if not root:
        #     return 0
        # q = deque()
        # q.append(root) 
        # level = 0
        # while q:
        #     level += 1
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if  node.left:
        #             q.append(node.left) 
        #         if  node.right:
        #             q.append(node.right)
        # return level 
    #DFS + list/set
        if not root:
            return 0
        rtinfo = [root, 1]
        lsts = []
        lsts.append(rtinfo)
        depth = 1
        while lsts:
            for i in range(len(lsts)):
                node, level = lsts.pop()
                depth = max(depth, level)
                if node.left:
                    lsts.append([node.left, level + 1])
                if node.right:
                    lsts.append([node.right, level + 1])   
        return depth



