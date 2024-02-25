# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from clrs.leetcode.utils.nodes import TreeNode


class Solution:
    def __init__(self) -> None:
        self.ans = None

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def dfs(node):
            if node == None:
                return False
            lson = dfs(node.left)
            rson = dfs(node.right)
            if (lson and rson) or (
                (node.val == p.val or node.val == q.val) and (lson or rson)
            ):
                self.ans = node
            return lson or rson or (node.val == p.val or node.val == q.val)

        dfs(root)
        return self.ans
