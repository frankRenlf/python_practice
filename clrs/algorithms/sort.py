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


class Sorts:

    def quick(self, arr):
        self.quick_sort(arr, 0, len(arr) - 1)

    def quick_sort(self, arr, left, right):
        if left < right:
            i = left
            j = right
            pivot = arr[left]
            while i < j:
                while i < j and arr[j] >= pivot:
                    j -= 1
                arr[i] = arr[j]
                while i < j and arr[i] <= pivot:
                    i += 1
                arr[j] = arr[i]
            arr[i] = pivot
            self.quick_sort(arr, left, i - 1)
            self.quick_sort(arr, i + 1, right)

    def merge(self, arr):
        self.merge_sort(arr, 0, len(arr) - 1)

    def merge_sort(self, arr, left, right):
        if left < right:
            mid = (right + left) >> 1
            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self.combine(arr, left, mid, right)

    def combine(self, arr, left, mid, right):
        # 2 4, 1 3 14 23
        tmp = list()
        start = left
        middle = mid
        length = right - left + 1
        while start <= mid or middle + 1 <= right:
            if start > mid:
                tmp.append(arr[middle + 1])
                middle += 1
                continue
            if middle + 1 > right:
                tmp.append(arr[start])
                start += 1
                continue
            if arr[start] < arr[middle + 1]:
                tmp.append(arr[start])
                start += 1
            else:
                tmp.append(arr[middle + 1])
                middle += 1
        for i in range(length):
            arr[left + i] = tmp[i]
