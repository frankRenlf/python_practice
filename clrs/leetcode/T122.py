# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/1 09:12 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(n):
            pre_i_0 = dp_i_0
            pre_i_1 = dp_i_1
            dp_i_0 = max(pre_i_0, pre_i_1 + prices[i])
            dp_i_1 = max(pre_i_1, pre_i_0 - prices[i])
        return dp_i_0
# if __name__ == "__main__":
