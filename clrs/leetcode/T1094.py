# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/2 01:43 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        to_max = max(trip[2] for trip in trips)
        dif = [0] * (to_max + 1)
        for t in trips:
            dif[t[1]] += t[0]
            dif[t[2]] -= t[0]
        cnt = 0
        for d in dif:
            cnt += d
            if cnt > capacity:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))
