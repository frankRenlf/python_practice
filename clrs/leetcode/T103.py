# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from clrs.leetcode.utils.Node import TreeNode
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque()
        q.append(root)
        depth = 0
        while len(q):
            l = len(q)
            cur = []
            while l:
                node = q.popleft()
                cur.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                l -= 1
            if depth % 2 != 0:
                cur.reverse()
            ans.append(cur)
            depth += 1
        return ans


c = {
    "Content-Length": "337",
    "Content-Type": "application/json; charset=utf-8",
    "request-id": "807a46d2-bf44-4a8e-ad6b-eb732a5552de",
    "api-supported-versions": "1",
    "x-envoy-upstream-service-time": "382",
    "apim-request-id": "807a46d2-bf44-4a8e-ad6b-eb732a5552de",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
    "x-content-type-options": "nosniff",
    "x-ms-region": "West US",
    "x-ratelimit-remaining-requests": "23",
    "x-ratelimit-remaining-tokens": "21928",
    "Date": "Fri, 16 Feb 2024 07:08:21 GMT",
}

b'{"error":{"code":"BadRequest","message":"The response was filtered due to the prompt triggering Azure OpenAI\'s content management policy. Please modify your prompt and retry. To learn more about our content filtering policies please read our documentation: \\r\\nhttps://go.microsoft.com/fwlink/?linkid=2198766.","param":null,"type":null}}'
