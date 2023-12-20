# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/11 00:26 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate(arr):
    root = ListNode(arr[0])
    cur = root
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        cur.next = node
        cur = cur.next
    return root


if __name__ == "__main__":
    root = generate([1, 2, 3, 3, 4, 4, 5])
    print()
