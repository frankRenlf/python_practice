# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/21 09:41 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import bisect


class SnapshotArray:

    def __init__(self, length: int):
        # 初始化字典数组和 id
        self.arr = [{0: 0} for _ in range(length)]
        self.sid = 0

    def set(self, index: int, val: int) -> None:
        # 设置当前快照的元素值
        self.arr[index][self.sid] = val

    def snap(self) -> int:
        # 每次快照 id 加 1
        self.sid += 1
        # 返回上一个快照 id
        return self.sid - 1

    def get(self, index: int, snap_id: int) -> int:
        # 选择要查找的元素的字典
        d = self.arr[index]
        # 如果快照恰好存在, 直接返回
        if snap_id in d:
            return d[snap_id]
        # 不存在则进行二分搜索, 查找快照前最后一次修改
        k = list(d.keys())
        i = bisect.bisect_left(k, snap_id)
        return d[k[i - 1]]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# if __name__ == "__main__":
