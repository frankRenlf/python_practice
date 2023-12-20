# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/20 09:10 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List
from collections import Counter


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        cnt = len(s)
        if len(words) != cnt:
            return False
        for i, word in enumerate(words):
            if s[i] != word[0]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAcronym(words = ["never","gonna","give","up","on","you"], s = "ngguoy"))
    print("1234"[0])
