# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/14 08:54 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        s = set(map(tuple, queens))
        ans = []
        for dx, dy in (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1):
            x, y = king[0] + dx, king[1] + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in s:
                    ans.append([x, y])
                    break
                x += dx
                y += dy
        return ans

# if __name__ == "__main__":
