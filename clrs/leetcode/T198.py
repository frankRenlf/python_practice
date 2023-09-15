# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/16 01:04 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp0 = [0] * n
        dp0[0] = nums[0]
        dp0[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp0[i] = max(dp0[i - 1], dp0[i - 2] + nums[i])
        return dp0[n - 1]
# if __name__ == "__main__":
