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
        if (n := len(jobDifficulty)) < d: return -1

        def dfs(k, d_):
            if d_ == 1: return max(jobDifficulty[k:])
            return min(max(jobDifficulty[k: i]) + dfs(i, d_ - 1) for i in range(k + 1, n - d_ + 2))

        return dfs(0, d)
