# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/28 00:44 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        arrange_list = sorted(intervals, key=lambda row: row[0])
        res = []
        left = 0
        right = 0
        n = len(intervals)
        while right < n:
            ele = [arrange_list[left][0], arrange_list[right][1]]
            while right < n and ele[1] >= arrange_list[right][0]:
                ele[1] = max(ele[1], arrange_list[right][1])
                right += 1
            res.append(ele)
            left = right
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
