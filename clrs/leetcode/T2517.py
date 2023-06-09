# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/1 09:06 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from math import inf
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        left, right = 0, price[-1] - price[0]
        while left < right:
            mid = (left + right + 1) // 2
            if self.check(price, k, mid):
                left = mid
            else:
                right = mid - 1
        return left

    def check(self, price: List[int], k: int, tastiness: int) -> bool:
        prev = -inf
        cnt = 0
        for p in price:
            if p - prev >= tastiness:
                cnt += 1
                prev = p
        return cnt >= k
