# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/23 09:10 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for detail in details:
            if int(detail[-4:-2]) > 60:
                cnt += 1
        # print(1 for info in details if int(info[11:13]) > 60)
        return cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSeniors(details=["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
