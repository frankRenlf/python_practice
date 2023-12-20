# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/20 14:41 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 2
        fast = 2
        n = len(nums)
        if n <= 2:
            return n
        while fast < n:
            while nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
            fast += 1
        return slow
    # if __name__ == "__main__":
