# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/16 10:17 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
import math
from functools import cache


def binary_digit_sum(n):
    return bin(n).count('1')


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        m = len(num2)
        up_limit = list(map(int, num2))
        down_limit = list(map(int, num1.zfill(m)))
        mod = 10 ** 9 + 7

        @cache
        def f(i=0, s=0, valid=False, dlimit=True, ulimit=True):
            if i == m:
                return int(valid and min_sum <= s <= max_sum)
            down = down_limit[i] if dlimit else 0
            up = up_limit[i] if ulimit else 9
            ans = 0
            for d in range(down, up + 1):
                ans = (ans + f(i + 1, s + d, valid or d != 0, dlimit and d == down, ulimit and d == up)) % mod
            return ans

        return f()

# if __name__ == "__main__":
#     sol = Solution()
#     (sol.count(num1="1", num2="5", min_num=1, max_num=5))
