# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/22 08:58 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        cnt = min(money // 7, children)
        money -= cnt * 7
        children -= cnt
        if (children == 0 and money > 0) or (children == 1 and money == 3):
            cnt -= 1
        return cnt

# if __name__ == "__main__":
