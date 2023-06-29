# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/29 08:25 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum): return []
        n = len(colsum)
        lstupper, lstlower = [0] * n, [0] * n
        upper -= colsum.count(2)
        if upper < 0: 
            return []
        for i, v in enumerate(colsum):
            if v == 2:
                lstupper[i] = lstlower[i] = 1
            if v == 1:
                if upper:
                    lstupper[i] = 1
                    upper -= 1
                else:
                    lstlower[i] = 1
        return [] if upper else [lstupper, lstlower]
