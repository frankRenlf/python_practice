from typing import List
import heapq


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        q = list()
        ans, hp, delay = 0, 1, 0
        for num in nums:
            if num < 0:
                heapq.heappush(q, num)
            hp += num
            if hp <= 0:
                ans += 1
                delay += q[0]
                hp -= heapq.heappop(q)
        hp += delay
        return -1 if hp <= 0 else ans
