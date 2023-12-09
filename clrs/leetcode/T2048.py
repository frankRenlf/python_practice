# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/9 10:15 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 1224445):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i

# if __name__ == "__main__":
