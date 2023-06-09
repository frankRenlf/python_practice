# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/28 08:40 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def merge(f: List[int], g: List[int], k: int) -> List[int]:
            left, right, thres = f[0] + g[0], f[-1] + g[-1], 0
            k = min(k, len(f) * len(g))
            while left <= right:
                mid = (left + right) // 2
                rptr, cnt = len(g) - 1, 0
                for lptr, x in enumerate(f):
                    while rptr >= 0 and x + g[rptr] > mid:
                        rptr -= 1
                    cnt += rptr + 1

                if cnt >= k:
                    thres = mid
                    right = mid - 1
                else:
                    left = mid + 1

            ans = list()
            for i, fi in enumerate(f):
                for j, gj in enumerate(g):
                    if (total := fi + gj) < thres:
                        ans.append(total)
                    else:
                        break

            ans += [thres] * (k - len(ans))
            ans.sort()
            return ans

        prev = mat[0]
        for i in range(1, len(mat)):
            prev = merge(prev, mat[i], k)
        return prev[k - 1]
