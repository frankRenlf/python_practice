# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/27 10:28 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
