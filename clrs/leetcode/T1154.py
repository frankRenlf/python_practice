# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/31 09:46 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        arr = date.split("-")
        year, month, day = [int(x) for x in date.split('-')]
        amount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            amount[1] += 1

        ans = sum(amount[:month - 1])
        return ans + day
# if __name__ == "__main__":
