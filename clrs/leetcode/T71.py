# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/20 13:40 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import queue


class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = list()
        for el in arr:
            if el == '..':
                if stack:
                    stack.pop()
            elif el and el != '.':
                stack.append(el)
        return '/' + '/'.join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath(path="/a//./b/../../c/a"))
