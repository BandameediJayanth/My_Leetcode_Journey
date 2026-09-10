# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def subtree_info(self, root):
        if not root:
            return 0,0,0
        
        lc , ls, lans = self.subtree_info(root.left)
        rc , rs , rans= self.subtree_info(root.right)

        ans = lans + rans
        cnt = 1 + lc + rc
        ts = root.val + ls + rs

        if root.val == ts // cnt:
            ans += 1
        

        return cnt, ts, ans
    def averageOfSubtree(self, root: TreeNode) -> int:
        _, _ , ans = self.subtree_info(root)
        return ans