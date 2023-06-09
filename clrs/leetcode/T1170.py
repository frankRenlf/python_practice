# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/10 12:40 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from bisect import bisect_right
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        a = sorted(s.count(min(s)) for s in words)
        print(a)
        return [len(a) - bisect_right(a, q.count(min(q))) for q in queries]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSmallerByFrequency(["bbb", "cc"], ["a", "aa", "aaa", "aaaa"]))
    s = "aaabbbbcdd"
    print(s.count(min(s)))
