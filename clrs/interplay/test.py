# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/4 09:02 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description :
"""

from collections import Counter


class PlayCounter:
    def test_counter(self):
        cnt1 = Counter([1, 2, 3, 4, 4, 1])
        cnt2 = Counter("acbcdefacde")

        if len(cnt2) > 0:
            cnt_1 = sorted(cnt2.items(), key=lambda x: x[1], reverse=True)
            print(cnt_1)
        else:
            print("Counter is empty")


if __name__ == '__main__':
    pc = PlayCounter()
    pc.test_counter()
