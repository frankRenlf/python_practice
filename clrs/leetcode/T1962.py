# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/23 09:53 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from heapq import heapify, heappop, heappush
from typing import List
from queue import PriorityQueue


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        q = PriorityQueue()
        for p in piles:
            q.put(-p)
        res = sum(piles)
        while k and not q.empty():
            k -= 1
            p = -q.get()
            add = (p // 2)
            res -= add
            q.put(-(p - add))
        return res

    def minStoneSum_fast(self, piles: List[int], k: int) -> int:
        heap = [-a for a in piles]
        heapify(heap)
        for i in range(k):
            a = -heappop(heap)
            a = a - a // 2
            heappush(heap, -a)
        return -sum(heap)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minStoneSum(piles=[5, 4, 9], k=2))
