# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/22 10:59 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            pivot = guess(mid)
            if pivot > 0:
                left = mid + 1
            else:
                right = mid
        return right
# if __name__ == "__main__":
