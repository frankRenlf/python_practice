from typing import List


class Solution:
    def addPosibinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        left = max(len(arr1), len(arr2))
        right = min(len(arr1), len(arr2))
        ret = [left + 1]
        add = 0
        while left >= 0:
            cur = arr1[left] + arr2[left] + add
            if cur >= 2:
                ret[left] = cur - 2
                add = 1
            else:
                ret[left] = cur
                add = 0
        return ret

    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        left = max(len(arr1), len(arr2))
        right = min(len(arr1), len(arr2))
        ret = [left + 1]
        add = 0
        for i in range(right):
            cur = arr1[i] + arr2[i] + add
            if cur >= 2:
                ret[i] = cur - 2
                add = 1
            else:
                ret[i] = cur
                add = 0
