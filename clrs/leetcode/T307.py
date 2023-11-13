# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/13 10:03 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List
import numpy as np


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.cumulate = [self.nums[0]] * self.n
        for i in range(1, self.n):
            self.cumulate[i] = (self.cumulate[i - 1] + self.nums[i])

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        for i in range(index, self.n):
            self.cumulate[i] = (self.cumulate[i - 1] + self.nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.cumulate[right] - self.cumulate[left] + self.nums[left]


class NumArray2:
    def __init__(self, nums: List[int]):
        self.arr = np.array(nums)

    def update(self, index: int, val: int) -> None:
        self.arr[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return int(np.sum(self.arr[left: right + 1]))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
if __name__ == "__main__":
    obj = NumArray([1, 3, 5, 2])
    print(obj.cumulate)
