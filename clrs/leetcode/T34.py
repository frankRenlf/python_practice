# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/20 17:19 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        l = left
        right = n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return [l, right]


if __name__ == "__main__":
    import bisect

    sorted_list = [1, 2,4]
    new_element = 3

    # 使用 bisect_left 找到插入新元素的位置
    position = bisect.bisect_left(sorted_list, new_element)
    position2 = bisect.bisect_right(sorted_list, new_element)

    print(position, position2)  # 输出应该插入新元素的索引
