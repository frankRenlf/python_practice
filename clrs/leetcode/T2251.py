# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/28 11:40 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        e = max(people)
        arr = [0] * (e + 1)
        for i in range(1, e + 1):
            num = 0
            for sub in flowers:
                if sub[0] <= i <= sub[1]:
                    num += 1
            arr[i] = num
        res = []
        for i in people:
            res.append(arr[i])
        return res

    def fullBloomFlowers2(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([start for start, _ in flowers])
        ends = sorted([end for _, end in flowers])
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in people]


if __name__ == "__main__":
    sol = Solution()
    print(sol.fullBloomFlowers(flowers=[[1, 10], [3, 3]], people=[3, 3, 2]))
