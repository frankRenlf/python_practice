# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/20 17:52 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""

import bisect


class TimeMap:

    def __init__(self):
        self.ts = list()
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ts.append(timestamp)
        self.mp[timestamp] = {key: value}

    def get(self, key: str, timestamp: int) -> str:
        position = bisect.bisect_left(self.ts, timestamp)
        if position >= len(self.ts) or self.ts[position] != timestamp:
            position -= 1
        while position >= 0:
            res = self.mp.get(self.ts[position]).get(key, None)
            if res:
                return res
            position -= 1
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    param_2 = obj.get("foo", 1)
