# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/21 09:00 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from collections import deque
from typing import List


class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        def judge(board: List[List[str]], x: int, y: int, dx: int, dy: int) -> bool:
            x += dx
            y += dy
            while 0 <= x < len(board) and 0 <= y < len(board[0]):
                if board[x][y] == "X":
                    return True
                elif board[x][y] == ".":
                    return False
                x += dx
                y += dy
            return False

        def bfs(board: List[str], px: int, py: int) -> int:
            board = [list(row) for row in board]
            cnt = 0
            q = deque([(px, py)])
            board[px][py] = "X"

            while q:
                tx, ty = q.popleft()
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == dy == 0:
                            continue
                        if judge(board, tx, ty, dx, dy):
                            x, y = tx + dx, ty + dy
                            while board[x][y] != "X":
                                q.append((x, y))
                                board[x][y] = "X"
                                x += dx
                                y += dy
                                cnt += 1
            return cnt

        res = 0
        for i in range(len(chessboard)):
            for j in range(len(chessboard[0])):
                if chessboard[i][j] == ".":
                    res = max(res, bfs(chessboard, i, j))
        return res
