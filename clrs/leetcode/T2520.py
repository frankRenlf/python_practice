# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/26 09:00 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def countDigits(self, num: int) -> int:
        arr = []

        for i in range(1, min(num, 9) + 1):
            if num % i == 0:
                arr.append(i)
        tmp = num
        res = 0
        while tmp:
            p = tmp % 10
            tmp //= 10
            if p in arr:
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDigits(1248))
