# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/28 09:46 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        total = sum(gifts)
        inv = [-gifts[i] for i in range(len(gifts))]
        heapq.heapify(inv)
        sub = 0
        while k > 0:
            k -= 1
            value = -heapq.heappop(inv)
            residue = math.floor(math.sqrt(value))
            heapq.heappush(inv, -residue)
            sub += value - residue
        return total - sub

    def pickGifts2(self, gifts: List[int], k: int) -> int:
        q = [-gift for gift in gifts]
        heapq.heapify(q)
        while k:
            x = heapq.heappop(q)
            heapq.heappush(q, -int(math.sqrt(-x)))
            k -= 1
        return -sum(q)


if __name__ == "__main__":
    sol = Solution()
    print(sol.pickGifts(gifts=[1, 1, 1, 1], k=4))
