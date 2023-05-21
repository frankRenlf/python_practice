# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/21 08:04 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description :
"""
from typing import List


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        cnt = max(vat)
        res = int('inf')
        if cnt == 0:
            return 0
        for i in range(1, cnt + 1):
            total = i
            for j in range(n):
                total += max(0, (vat[j] + i - 1) // j - bucket[j])
            res = min(res, total)
        return res
