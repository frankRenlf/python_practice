# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/8 01:05 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list_dict = {}
        for k, v in enumerate(numbers):
            list_dict[v] = k
        for k, v in enumerate(numbers):
            if target - v in list_dict:
                return [k + 1, list_dict[target - v] + 1]
        return [-1, -1]