# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/25 22:23 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description :
"""
from typing import List


class Merge:

    def __init__(self, array: List[int]):
        self.arr = array

    def sort(self) -> List[int]:
        self.merge_sort(0, len(self.arr) - 1)
        return self.arr

    def merge_sort(self, left, right):
        if left < right:
            mid = (right + left) >> 1
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        # 2 4, 1 3 14 23
        tmp = list()
        start = left
        middle = mid
        length = right - left + 1
        while start <= mid or middle + 1 <= right:
            if start > mid:
                tmp.append(self.arr[middle + 1])
                middle += 1
                continue
            if middle + 1 > right:
                tmp.append(self.arr[start])
                start += 1
                continue
            if self.arr[start] < self.arr[middle + 1]:
                tmp.append(self.arr[start])
                start += 1
            else:
                tmp.append(self.arr[middle + 1])
                middle += 1
        for i in range(length):
            self.arr[left + i] = tmp[i]
