# -*- coding: UTF-8 -*-
"""
@Project : python_practice 
@env     : PyCharm
@File    : TreeNode.py
@Author  : Frank
@Date    : 2023/5/20 08:03 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_perfect_binary_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    # 使用队列按层次构建树
    while i < len(arr):
        current = queue.pop(0)

        # 添加左子节点
        if i < len(arr):
            current.left = TreeNode(arr[i])
            queue.append(current.left)
            i += 1

        # 添加右子节点
        if i < len(arr):
            current.right = TreeNode(arr[i])
            queue.append(current.right)
            i += 1

    return root
