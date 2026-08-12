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
        dic = {val:idx for idx, val in enumerate(inorder)}

        def dfs(l_pre, r_pre, l_in, r_in):
            if l_pre - r_pre == 0:
                return TreeNode(preorder[l_pre])
            if r_pre < l_pre:
                return None
            root = TreeNode(preorder[l_pre])
            root_idx = dic[root.val]
            left_len = root_idx - l_in
            root.left = dfs(l_pre + 1, l_pre + left_len, l_in, l_in + left_len - 1)
            root.right = dfs(l_pre + left_len + 1, r_pre, l_in + left_len + 1, r_in)
            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)