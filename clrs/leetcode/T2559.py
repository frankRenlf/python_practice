# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/2 08:00 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        w = [0] * len(words)
        set1 = set()
        for i in ['a', 'e', 'i', 'o', 'u']:
            set1.add(i)
        for i, el in enumerate(words):
            if el[0] in set1 and el[-1] in set1:
                w[i] = 1
            else:
                w[i] = 0
        ret = [0] * len(queries)
        for i, tp in enumerate(queries):
            for j in range(tp[0], tp[1] + 1):
                ret[i] += w[j]
        return ret

    def vowelStrings_presum(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def isVowelString(word):
            return isVowelLetter(word[0]) and isVowelLetter(word[-1])

        def isVowelLetter(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

        n = len(words)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            value = 1 if isVowelString(words[i]) else 0
            prefix_sums[i + 1] = prefix_sums[i] + value
        ans = []
        for i in range(len(queries)):
            start, end = queries[i]
            ans.append(prefix_sums[end + 1] - prefix_sums[start])
        return ans
