# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/30 10:36 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        prev = ans = 0
        for p, g in sorted(zip(plantTime, growTime), key=lambda x: -x[1]):
            ans = max(ans, prev + p + g)
            prev += p
        return ans

# if __name__ == "__main__":
