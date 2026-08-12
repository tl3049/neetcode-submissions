# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#preorder:root, left, right
#inorder: left, root, right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        def dfs(st_pre, ed_pre, st_in, ed_in):
            if ed_pre - st_pre == 0:
                return TreeNode(preorder[st_pre])
            if ed_pre < st_pre:
                return None
            root = TreeNode(preorder[st_pre])
            rt_idx_inorder = dic[root.val]
            l_len = rt_idx_inorder - st_in
            root.left = dfs(st_pre + 1, st_pre + l_len, st_in, st_in + l_len - 1)
            root.right = dfs(st_pre + l_len + 1, ed_pre, st_in + l_len + 1, ed_in)
            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)