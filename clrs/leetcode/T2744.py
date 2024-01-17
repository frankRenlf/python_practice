# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/17 09:11 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        seen = set()
        for i, word in enumerate(words):
            if word[::-1] in seen:
                ans += 1
            seen.add(word)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumNumberOfStringPairs(["ac", "ca", "dc", "ca", "zz"]))
