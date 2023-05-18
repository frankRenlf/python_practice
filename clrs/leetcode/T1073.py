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
            left -= 1
        return ret

    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i1 = len(arr1) - 1
        i2 = len(arr2) - 1
        ret = list()
        add = 0
        while i1 >= 0 or i2 >= 0 or add:
            cur = add
            if i1 >= 0:
                cur += arr1[i1]
            if i2 >= 0:
                cur += arr2[i2]

            if cur >= 2:
                ret.append(cur - 2)
                add = -1
            elif cur == -1:
                ret.append(1)
                add = 1
            else:
                ret.append(cur)
                add = 0
            i1 -= 1
            i2 -= 1
        while len(ret) > 0 and ret[-1] == 0:
            ret.pop()
        ret.reverse()
        return ret
