from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            cnt[t] += 1
            print(cnt)
        print("final", cnt)
        return max(cnt.values())

    def maxEqualRowsAfterFlips1(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            key = []
            for j in range(n):
                key.append(matrix[i][j] ^ matrix[i][0])
            cnt[key.__str__()] += 1
        return max(cnt.values())
