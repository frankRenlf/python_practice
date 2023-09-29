# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/29 10:22 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        length = len(flowerbed)
        r = length - 1
        l = r
        while l >= 0:
            r = l
            while l >= 0 and flowerbed[l] == 0:
                l -= 1
            if l == -1 and r == length - 1:
                res += (r - l + 1) // 2
            elif r == length - 1 or l == -1:
                res += abs(r - l) // 2
            else:
                res += abs(r - l - 1) // 2
            l -= 1
        return res >= n


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1))
