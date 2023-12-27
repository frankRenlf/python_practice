# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/28 07:43 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        f = nums[:]
        ans = sum(f)

        for k in range(1, n):
            for i in range(n):
                f[i] = min(f[i], nums[(i + k) % n])
            ans = min(ans, k * x + sum(f))

        return ans

# if __name__ == "__main__":
