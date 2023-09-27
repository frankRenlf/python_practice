# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/27 09:04 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def filterRestaurants(self,
                          restaurants: List[List[int]],
                          veganFriendly: int,
                          maxPrice: int,
                          maxDistance: int) -> List[int]:
        filter_ = []
        for index, el in enumerate(restaurants):
            if veganFriendly and not el[2]:
                continue
            if el[3] <= maxPrice and el[4] <= maxDistance:
                filter_.append(el)
        filter_.sort(key=lambda res: (res[1], res[0]), reverse=True)
        return [res[0] for res in filter_]


if __name__ == "__main__":
    arr = [[1, 2, 3, 4],
           [1, 2, 3, 4]]
    print(arr[0][:])
