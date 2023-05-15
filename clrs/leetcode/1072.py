from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = Counter()
        for i in range(m):
            value = 0
            for j in range(n):
                # 如果 matrix[i][0] 为 1，则对该行元素进行翻转
                value = value * 10 + (matrix[i][j] ^ matrix[i][0])
            count[value] += 1
        return max(count.values())
