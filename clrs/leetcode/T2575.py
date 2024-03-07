from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        div = [0] * n
        cur = 0
        for i in range(0, n):
            cur = (cur * 10 + int(word[i])) % m
            if cur == 0:
                div[i] = 1
        return div


if __name__ == "__main__":
    sol = Solution()
    print(sol.divisibilityArray(word="998244353", m=3))
