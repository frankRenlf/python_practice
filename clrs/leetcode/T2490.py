# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/30 10:06 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence != sentence.strip():
            return False
        arr = sentence.split(' ')
        n = len(arr)
        for i in range(n - 1):
            if arr[i][-1] != arr[i + 1][0]:
                return False
        return arr[0][0] == arr[n - 1][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isCircularSentence("leetcode es sool"))
