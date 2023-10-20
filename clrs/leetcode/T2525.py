# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/20 10:06 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def categorizeBox(self, length, width, height, mass):
        maxd = max(length, width, height)
        vol = length * width * height
        isBulky = maxd >= 10000 or vol >= 10 ** 9
        isHeavy = mass >= 100
        if isBulky and isHeavy:
            return 'Both'
        if isBulky:
            return 'Bulky'
        if isHeavy:
            return 'Heavy'
        return 'Neither'

# if __name__ == "__main__":
