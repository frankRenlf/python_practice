# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/16 10:42 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l = r = 0
        n = len(nums)
        res = 0
        while l < n and r < n:
            while (r + 1 < n
                   and nums[l] % 2 == 0
                   and nums[r] <= threshold
                   and nums[r] % 2 != nums[r + 1] % 2):
                r += 1
            res = max(res, r - l + 1)
            l = r = r + 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestAlternatingSubarray(nums=[3, 2, 5, 4], threshold=5))
