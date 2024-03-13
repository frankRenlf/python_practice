from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        mp = Counter(s)
        mp["1"] -= 1
        return "1" * mp["1"] + "0" * mp["0"] + "1"


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumOddBinaryNumber("010"))
