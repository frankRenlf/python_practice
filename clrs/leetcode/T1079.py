from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        tile = set(tiles)
        print(count)
        print(tile)
        return self.dfs(tile, count, len(tiles)) - 1

    def dfs(self, tile, cnt, level) -> int:
        if level == 0:
            return 1
        total = 1
        for i in tile:
            if cnt[i] > 0:
                cnt[i] -= 1
                total += self.dfs(tile, cnt, level - 1)
                cnt[i] += 1
        return total
