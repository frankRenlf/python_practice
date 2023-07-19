# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/20 00:12 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import sys
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        # 对坐标为 0 处的元素单独处理，避免考虑子数组为空的情况
        leftMax[0], leftSum = nums[0], nums[0]
        pre_map = [-sys.maxsize] * n
        pre_map[0], res = nums[0], nums[0]
        for i in range(1, n):
            pre_map[i] = max(pre_map[i - 1] + nums[i], nums[i])
            res = max(res, pre_map[i])
            leftSum += nums[i]
            leftMax[i] = max(leftMax[i - 1], leftSum)
        # 从右到左枚举后缀，固定后缀，选择最大前缀
        rightSum = 0
        for i in range(n - 1, 0, -1):
            rightSum += nums[i]
            res = max(res, rightSum + leftMax[i - 1])
        return res
