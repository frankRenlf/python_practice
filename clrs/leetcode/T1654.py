# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/30 01:12 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import sys
from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        vis = set()
        s = set(forbidden)
        q = deque()
        vis.add((0, 0))
        q.append((0, 0, 0))
        while q:
            poll = q.popleft()
            e, v, f = poll[0], poll[1], poll[2]
            if e == x:
                return v
            if (e + a, 0) not in vis and e + a <= (b + x) * 5 and e + a not in s:
                q.append((e + a, v + 1, 0))
                vis.add((e + a, 0))
            if (e - b, 1) not in vis and e - b > -1 and e - b not in s and f != 1:
                q.append((e - b, v + 1, 1))
                vis.add((e - b, 1))
        return -1


if __name__ == "__main__":
    sol = Solution()
    sol.minimumJumps([1], 1, 1, 1)
