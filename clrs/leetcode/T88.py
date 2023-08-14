# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/13 09:39 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
import sys
from typing import List


class Solution:
    def merge_forward(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cp = [0] * m
        cp[:] = nums1[:m]
        i = j = 0
        for k in range(m + n):
            add = 0
            n1 = cp[i] if i < m else sys.maxsize
            n2 = nums2[j] if j < n else sys.maxsize
            if n1 < n2:
                add = n1
                i += 1
            else:
                add = n2
                j += 1
            nums1[k] = add

    def merge_backward(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.merge_backward([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
