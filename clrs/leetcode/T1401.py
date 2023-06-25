# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/25 13:03 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""

import numpy as np


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        v_s = np.array([x1 + x2, y1 + y2]) / 2
        v_s_p = np.array([x2, y2]) - v_s
        v_s_c = abs(np.array([xCenter, yCenter]) - v_s)
        v_p_c = np.maximum(v_s_c - v_s_p, 0)
        return v_p_c @ v_p_c <= radius ** 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkOverlap(radius=1, xCenter=0, yCenter=0, x1=1, y1=-1, x2=3, y2=1))