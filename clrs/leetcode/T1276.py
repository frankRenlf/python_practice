# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/25 09:50 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        """
        4x 2y=ts
        x y = cs
        x=(ts-cs)/2
        y = cs-x
        """
        x = abs((tomatoSlices - 2 * cheeseSlices) // 2)
        y = abs(cheeseSlices - x)
        return [x, y] if 4 * x + 2 * y == tomatoSlices and x + y == cheeseSlices else []
# if __name__ == "__main__":
