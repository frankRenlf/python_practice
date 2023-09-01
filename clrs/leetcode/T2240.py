# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/1 10:59 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            return self.waysToBuyPensPencils(total, cost2, cost1)
        res, cnt = 0, 0
        while cnt * cost1 <= total:
            res += (total - cnt * cost1) // cost2 + 1
            cnt += 1
        return res

# if __name__ == "__main__":
