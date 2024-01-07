# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/7 21:19 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mg = Counter(magazine)
        for k, v in rn.items():
            if not mg.__contains__(k) or mg[k] < v:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct(ransomNote="aa", magazine="ab"))
