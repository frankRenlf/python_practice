# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/26 09:41 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        redundant = time % (n - 1)
        bos = 1 if (time / (n - 1)) % 2 == 0 else n
        if bos == 1:
            res = bos + redundant
        else:
            res = bos - redundant
        return res

    def passThePillow2(self, n: int, time: int) -> int:
        time %= (n - 1) * 2
        return time + 1 if time < n else n * 2 - time - 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.passThePillow(n=3, time=2))
