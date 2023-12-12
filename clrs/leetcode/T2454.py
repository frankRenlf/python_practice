# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/12 10:10 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
import math
from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        winner = [(math.inf, 0)]
        loser = [(math.inf, 0)]
        res = [-1] * len(nums)
        for i, num in enumerate(nums):
            while loser[-1][0] < num:
                res[loser.pop()[1]] = nums[i]
            temp = []
            while winner[-1][0] < num:
                temp.append(winner.pop())
            loser.extend(reversed(temp))
            winner.append((num, i))
        return res

    def nGreaterElement(self, nums: List[int]) -> List[int]:
        m = 2
        container = [[(math.inf, 0)] for _ in range(m)]
        res = [-1] * len(nums)
        for i, num in enumerate(nums):
            while container[-1][-1][0] < num:
                res[container[-1].pop()[1]] = nums[i]
            for j in range(m - 1):
                temp = []
                while container[j][-1][0] < num:
                    temp.append(container[j].pop())
                container[j + 1].extend(reversed(temp))
            container[0].append((num, i))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.nGreaterElement(nums=[2, 4, 0, 9, 6]))
