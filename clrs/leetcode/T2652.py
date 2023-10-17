# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/17 10:08 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def f(m: int) -> int:
            return (m + n // m * m) * (n // m) // 2

        return f(3) + f(5) + f(7) - f(3 * 5) - f(3 * 7) - f(5 * 7) + f(3 * 5 * 7)

# if __name__ == "__main__":
