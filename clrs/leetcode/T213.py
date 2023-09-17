# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/17 09:47 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp0 = [0] * n
        dp1 = [0] * n
        dp0[0] = nums[0]
        dp0[1] = max(nums[0], nums[1])

        for i in range(2, n - 1):
            dp0[i] = max(dp0[i - 1], dp0[i - 2] + nums[i])
        dp1[1] = nums[1]
        dp1[2] = max(nums[2], nums[1])
        for i in range(3, n):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        return max(dp0[n - 2], dp1[n - 1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))
