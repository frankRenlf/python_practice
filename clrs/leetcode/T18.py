# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/15 11:20 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def Search(i, target, oneSolution, notSelected):
            if target == 0 and len(oneSolution) == 4:
                output.append(oneSolution)
                return
            elif len(oneSolution) > 4 or i >= len(nums):
                return

            if target - nums[i] - (3 - len(oneSolution)) * nums[-1] > 0 or nums[i] in notSelected:
                Search(i + 1, target, oneSolution, notSelected)
            elif target - (4 - len(oneSolution)) * nums[i] < 0:
                return
            else:
                Search(i + 1, target, oneSolution, notSelected + [nums[i]])
                Search(i + 1, target - nums[i], oneSolution + [nums[i]], notSelected)

        Search(0, target, [], [])

        return output


if __name__ == "__main__":
    arr = [1, 2, 3]
    brr = [4, 5, 6]
    crr = arr + brr
    print(crr)
    arr[0] = 10
    print(crr)
