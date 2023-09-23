# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/23 09:21 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.lockNodeUser = [-1] * n
        self.children = [[] for _ in range(n)]
        for node, p in enumerate(parent):
            if p != -1:
                self.children[p].append(node)

    def lock(self, num: int, user: int) -> bool:
        if self.lockNodeUser[num] == -1:
            self.lockNodeUser[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if self.lockNodeUser[num] == user:
            self.lockNodeUser[num] = -1
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        res = self.lockNodeUser[num] == -1 and not self.hasLockedAncestor(num) and self.checkAndUnlockDescendant(num)
        if res:
            self.lockNodeUser[num] = user
        return res

    def hasLockedAncestor(self, num: int) -> bool:
        num = self.parent[num]
        while num != -1:
            if self.lockNodeUser[num] != -1:
                return True
            else:
                num = self.parent[num]
        return False

    def checkAndUnlockDescendant(self, num: int) -> bool:
        res = self.lockNodeUser[num] != -1
        self.lockNodeUser[num] = -1
        for child in self.children[num]:
            res |= self.checkAndUnlockDescendant(child)
        return res

# if __name__ == "__main__":
