from ast import List
from functools import reduce


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        # s = 0
        # for num in reversed(nums):
        #     if num <= s:
        #         s += num
        #     else:
        #         s = num
        # return s
        return reduce(lambda a, b: a + b if a >= b else b, reversed(nums))
