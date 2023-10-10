# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/10 09:16 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List
from collections import Counter


class Solution:

    def sumDistance_fast(self, nums: List[int], s: str, d: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        pos = [nums[i] - d if s[i] == 'L' else nums[i] + d for i in range(n)]
        pos.sort()
        return sum([(pos[i] - pos[i - 1]) * i * (n - i) for i in range(1, n)]) % mod

    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        direct = [1 if i == 'R' else -1 for i in list(s)]
        for i in range(d):
            # nums[:] += direct[:]
            for j in range(n):
                nums[j] += direct[j]
            self.check(nums, direct, n)
            print(direct)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res += abs(nums[i] - nums[j])
        return res % (10 ** 9 + 7)

    def check(self, nums, direct, n):
        mp = Counter(nums)
        print(mp)
        for i in range(n):
            if mp[nums[i]] > 1:
                direct[i] = -direct[i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumDistance(nums=[1, 0], s="RL", d=2))
