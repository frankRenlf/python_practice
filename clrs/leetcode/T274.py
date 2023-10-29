# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/29 09:02 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)
        while left < right:
            # +1 防止死循环
            mid = (left + right + 1) >> 1
            cnt = 0
            for v in citations:
                if v >= mid:
                    cnt += 1
            if cnt >= mid:
                # 要找的答案在 [mid,right] 区间内
                left = mid
            else:
                # 要找的答案在 [0,mid) 区间内
                right = mid - 1
        return left

# if __name__ == "__main__":
