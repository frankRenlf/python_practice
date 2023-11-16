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
        res, dp = 0, 0
        for l in range(len(nums) - 1, -1, -1):
            if nums[l] > threshold:
                dp = 0
            elif l == len(nums) - 1 or nums[l] % 2 != nums[l + 1] % 2:
                dp = dp + 1
            else:
                dp = 1
            res = dp if nums[l] % 2 == 0 and dp > res else res
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestAlternatingSubarray(nums=[3, 2, 5, 4], threshold=5))
