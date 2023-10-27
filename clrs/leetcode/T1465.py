# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/27 09:26 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def calMax(arr, boardr):
            res, pre = 0, 0
            for i in arr:
                res = max(i - pre, res)
                pre = i
            return max(res, boardr - pre)

        horizontalCuts.sort()
        verticalCuts.sort()
        return (calMax(horizontalCuts, h) * calMax(verticalCuts, w)) % (10 ** 9 + 7)

# if __name__ == "__main__":
