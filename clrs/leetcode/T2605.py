# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/5 08:53 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        def same() -> int:
            s = set(nums1) & set(nums2)
            return -1 if not s else min(s)

        if (x := same()) != -1:
            return x

        x = min(nums1)
        y = min(nums2)
        return min(x * 10 + y, y * 10 + x)

# if __name__ == "__main__":
