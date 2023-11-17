# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/18 01:17 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 计算一个数字的数位和
        def digit_sum(num: int) -> int:
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s

        map_ = {}  # 存储每个数位和的最大数字
        res = -1  # 结果，初始为-1，表示没有满足条件的数对
        for num in nums:
            ds = digit_sum(num)  # 计算当前数字的数位和
            if ds in map_:
                # 如果映射表中存在这个数位和，取映射表中存储的最大值和当前数字相加更新res
                res = max(res, num + map_[ds])
            map_[ds] = max(num, map_.get(ds, 0))  # 更新映射表中这个数位和对应的最大数字
        return res

# if __name__ == "__main__":
