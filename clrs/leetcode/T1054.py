from typing import List


class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        data = []
        print(Counter(barcodes).most_common())
        for i, j in Counter(barcodes).most_common():
            data += [i] * j
        print(data)
        l = len(data)
        print(l)
        ans = [0] * l
        ans[::2] = data[:(l + 1) // 2]
        ans[1::2] = data[(l + 1) // 2:]
        return ans

    def dfs(self, index, barcodes: List[int]):
        if index == len(barcodes):
            return
        barcodes[index] += 1
        self.dfs(self, index + 1, barcodes)
