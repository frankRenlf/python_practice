# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/21 09:09 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        res = 0
        prefix, suffix = [0] * n, [0] * n
        stack1, stack2 = [], []

        for i in range(n):
            while len(stack1) > 0 and maxHeights[i] < maxHeights[stack1[-1]]:
                stack1.pop()
            if len(stack1) == 0:
                prefix[i] = (i + 1) * maxHeights[i]
            else:
                prefix[i] = prefix[stack1[-1]] + (i - stack1[-1]) * maxHeights[i]
            stack1.append(i)
        for i in range(n - 1, -1, -1):
            while len(stack2) > 0 and maxHeights[i] < maxHeights[stack2[-1]]:
                stack2.pop()
            if len(stack2) == 0:
                suffix[i] = (n - i) * maxHeights[i]
            else:
                suffix[i] = suffix[stack2[-1]] + (stack2[-1] - i) * maxHeights[i]
            stack2.append(i)
            res = max(res, prefix[i] + suffix[i] - maxHeights[i])
        return res

# if __name__ == "__main__":