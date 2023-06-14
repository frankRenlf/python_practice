# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/14 09:18 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = right = 0
        for i, flip in enumerate(flips):
            right = max(right, flips[i])
            if right == i + 1:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTimesAllBlue([4, 4, 2, 4, 3]))
