# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/16 10:09 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from sortedcontainers import SortedDict


class CountIntervals:
    def __init__(self):
        self.mp = SortedDict()
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        interval_index = self.mp.bisect_right(right)
        if interval_index != 0:
            interval_index -= 1
        while interval_index < len(self.mp) and self.mp.keys()[interval_index] <= right \
                and self.mp.values()[interval_index] >= left:
            l, r = self.mp.items()[interval_index]
            left = min(left, l)
            right = max(right, r)
            self.cnt -= r - l + 1
            self.mp.popitem(interval_index)
            interval_index = self.mp.bisect_right(right)
            if interval_index != 0:
                interval_index -= 1
        self.cnt += right - left + 1
        self.mp[left] = right

    def count(self) -> int:
        return self.cnt

# if __name__ == "__main__":
