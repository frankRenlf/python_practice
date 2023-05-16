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
        n = len(jobDifficulty)
        if n < d:
            return -1
        elif n == d:
            return sum(jobDifficulty)

        return
