# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/27 09:32 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = len(count)
        total = sum(count)
        mean = 0.0
        median = 0.0
        min_num = 256
        max_num = 0
        mode = 0

        left = (total + 1) // 2
        right = (total + 2) // 2
        cnt = 0
        max_freq = 0
        sum_ = 0
        for i in range(n):
            sum_ += count[i] * i
            if count[i] > max_freq:
                max_freq = count[i]
                mode = i
            if count[i] > 0:
                if min_num == 256:
                    min_num = i
                max_num = i
            if cnt < right <= cnt + count[i]:
                median += i
            if cnt < left <= cnt + count[i]:
                median += i
            cnt += count[i]
        mean = sum_ / total
        median = median / 2.0
        return [min_num, max_num, mean, median, mode]
