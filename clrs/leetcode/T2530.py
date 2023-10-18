# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/18 09:16 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        minus_nums = [-num for num in nums]
        heapq.heapify(minus_nums)
        res = 0
        for _ in range(k):
            val = heapq.heappop(minus_nums)
            res += -val
            heapq.heappush(minus_nums, -((-val + 2) // 3))
        return res
# if __name__ == "__main__":
