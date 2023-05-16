"""
 * Created with IntelliJ IDEA.
 * @Project      : clrs
 * @Package      : 
 * @createTime   : 2023/5/16 8:05
 * @version      : 1.0
 * @author       : Frank.Ren
 * @Email        : sc19lr@leeds.ac.uk
 * @github       : https://github.com/frankRenlf
 * @Description  : 
"""
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if (n := len(jobDifficulty)) < d:
            return -1

        def dfs(left, remain):
            if remain == 1:
                return max(jobDifficulty[left:])
            return min(max(jobDifficulty[left:i]) + dfs(i, remain - 1) for i in range(left + 1, n - remain + 2))

        return dfs(0, d)
