# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/4 11:16 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from clrs.leetcode.utils.nodes import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.prefix = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node is None:
                return
            inorder(node.right)
            self.prefix += node.val
            node.val = self.prefix
            inorder(node.left)

        inorder(root)
        return root


if __name__ == "__main__":
    root0 = TreeNode(0)

    root0.right = root = TreeNode(2)
    root.right = TreeNode(3)
    root.left = TreeNode(1)
    sol = Solution()
    sol.bstToGst(root0)
    print(root0)


c = {
    "id": "chatcmpl-8t57NE0JFw9CTVBCqCXLMTIbnkMyV",
    "object": "chat.completion",
    "created": 1708138405,
    "model": "gpt-4",
    "prompt_filter_results": [
        {
            "prompt_index": 0,
            "content_filter_results": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": False, "severity": "safe"},
            },
        }
    ],
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {"role": "assistant"},
            "content_filter_results": {},
        }
    ],
    "usage": {"prompt_tokens": 4234, "completion_tokens": 0, "total_tokens": 4234},
    "system_fingerprint": "fp_68a7d165bf",
}
