# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/3 08:55 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        c = n - k
        p = c
        cmp = sum([cardPoints[i] for i in range(c)])
        least = cmp
        while p < n:
            cmp += -cardPoints[p - c] + cardPoints[p]
            least = min(least, cmp)
            p += 1
        return sum(cardPoints) - least


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))
