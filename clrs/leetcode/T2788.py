# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/20 09:51 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            for w in word.split(separator):
                if w != "":
                    ans.append(w)
        return ans

    def splitWordsBySeparator2(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            res += [sub for sub in word.split(separator) if len(sub)]
        return res

# if __name__ == "__main__":
