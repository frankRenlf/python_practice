# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/24 00:18 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        T, N, M = 243, 5, 6
        # 邻居间的分数
        score = [
            [0, 0, 0],
            [0, -60, -10],
            [0, -10, 40],
        ]

        tot = 3 ** n
        mask_bits = [[0] * N for _ in range(T)]
        iv_count, ev_count = [0] * T, [0] * T
        inner_score = [0] * T
        inter_score = [[0] * T for _ in range(T)]

        def init_data() -> None:
            # 计算行内分数
            for mask in range(tot):
                mask_tmp = mask
                for i in range(n):
                    x = mask_tmp % 3
                    mask_bits[mask][i] = x
                    mask_tmp //= 3
                    if x == 1:
                        iv_count[mask] += 1
                        inner_score[mask] += 120
                    elif x == 2:
                        ev_count[mask] += 1
                        inner_score[mask] += 40
                    if i > 0:
                        inner_score[mask] += score[x][mask_bits[mask][i - 1]]
            # 计算行间分数
            for i in range(tot):
                for j in range(tot):
                    for k in range(n):
                        inter_score[i][j] += score[mask_bits[i][k]][mask_bits[j][k]]

        def dfs(row: int, premask: int, iv: int, ev: int) -> int:
            if row == m or (iv == 0 and ev == 0):
                return 0

            res = 0
            for mask in range(tot):
                # mask 包含的内向人数不能超过 iv ，外向人数不能超过 ev
                if iv_count[mask] > iv or ev_count[mask] > ev:
                    continue
                res = max(res, dfs(row + 1, mask, iv - iv_count[mask], ev - ev_count[mask]) + inner_score[mask] +
                          inter_score[premask][mask])
            return res

        init_data()
        return dfs(0, 0, introvertsCount, extrovertsCount)
