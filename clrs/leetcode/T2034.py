# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/8 09:34 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import sys
from sortedcontainers import SortedList


class StockPrice:
    def __init__(self):
        self.price = SortedList()
        self.timePriceMap = {}
        self.maxTimestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timePriceMap:
            self.price.discard(self.timePriceMap[timestamp])
        self.price.add(price)
        self.timePriceMap[timestamp] = price
        self.maxTimestamp = max(self.maxTimestamp, timestamp)

    def current(self) -> int:
        return self.timePriceMap[self.maxTimestamp]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]

# if __name__ == "__main__":
