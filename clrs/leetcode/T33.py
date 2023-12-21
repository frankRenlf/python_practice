# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/21 11:30 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

# if __name__ == "__main__":
