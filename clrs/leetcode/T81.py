# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/20 16:21 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        s = 0
        e = n - 1
        while s <= e and target > nums[s]:
            s += 1
        while e >= 0 and target < nums[e]:
            e -= 1
        return (s < n and e >= 0) and (target == nums[s] or target == nums[e])


class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        n = len(nums)
        if n == 1:
            return nums[0] == target

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

# if __name__ == "__main__":
