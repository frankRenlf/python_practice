# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/29 12:19 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr = sorted(arr)
        dp = [1] * n
        res, mod = 0, 10 ** 9 + 7
        for i in range(n):
            left, right = 0, i - 1
            while left <= right:
                while right >= left and arr[left] * arr[right] > arr[i]:
                    right -= 1
                if right >= left and arr[left] * arr[right] == arr[i]:
                    if right != left:
                        dp[i] = (dp[i] + dp[left] * dp[right] * 2) % mod
                    else:
                        dp[i] = (dp[i] + dp[left] * dp[right]) % mod
                left += 1
            res = (res + dp[i]) % mod
        return res

# if __name__ == "__main__":
