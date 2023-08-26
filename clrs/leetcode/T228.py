# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/26 09:57 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution2:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def f(i: int, j: int) -> str:
            return str(nums[i]) if i == j else f'{nums[i]}->{nums[j]}'

        i = 0
        n = len(nums)
        ans = []
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            ans.append(f(i, j))
            i = j + 1
        return ans


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        pre = 0
        res = []
        i = 1
        while i < n:
            while i < n and nums[i - 1] + 1 == nums[i]:
                i += 1
            if i - 1 >= pre + 1:
                res.append(nums[pre].__str__() + "->" + nums[i - 1].__str__())
                pre = i
            elif i == pre:
                res.append(nums[pre].__str__())
                pre = i + 1
            i += 1
        if pre < n:
            res.append(nums[pre].__str__())
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0, 1, 2, 4, 5, 7]))
