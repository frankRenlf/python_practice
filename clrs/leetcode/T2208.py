# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/25 00:36 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half = sum(nums) / 2
        pq = []
        for num in nums:
            heappush(pq, -num)
        val = 0
        cnt = 0
        while val < half:
            x = -heappop(pq) / 2
            val += x
            heappush(pq, -x)
            cnt += 1
        return cnt
