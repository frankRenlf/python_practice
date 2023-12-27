# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/27 09:53 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1 = -1
        p2 = -1
        n = len(player1)
        s1 = s2 = 0
        for i in range(n):
            if p1 >= 0 and i - p1 <= 2:
                s1 += 2 * player1[i]
            else:
                s1 += player1[i]
            if player1[i] == 10:
                p1 = i
            if p2 >= 0 and i - p2 <= 2:
                s2 += 2 * player2[i]
            else:
                s2 += player2[i]
            if player2[i] == 10:
                p2 = i
        if s1 > s2:
            return 1
        if s1 < s2:
            return 2
        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isWinner(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2]))

"""
    1.e*coefficient
    2.normalise
"""