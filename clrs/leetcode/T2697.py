# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/13 08:47 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        arr = [s[n // 2]] * n
        for i in range(n // 2):
            arr[i] = arr[n - 1 - i] = min(s[i], s[n - i - 1])
        return ''.join(arr)


if __name__ == "__main__":
    sol = Solution()
    print(sol.makeSmallestPalindrome("egcfe"))
