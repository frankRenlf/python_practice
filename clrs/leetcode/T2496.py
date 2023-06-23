# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/23 08:44 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ret = 0
        for s in strs:
            if s.isdigit():
                ret = max(int(s), ret)
            else:
                ret = max(len(s), ret)
        return ret
