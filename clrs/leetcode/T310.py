import sys
from typing import List


class Solution1:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n
        maxDepth, node = 0, -1

        def dfs(x: int, pa: int, depth: int):
            nonlocal maxDepth, node
            if depth > maxDepth:
                maxDepth, node = depth, x
            parents[x] = pa
            for y in g[x]:
                if y != pa:
                    dfs(y, x, depth + 1)

        dfs(0, -1, 1)
        maxDepth = 0
        dfs(node, -1, 1)

        path = []
        while node != -1:
            path.append(node)
            node = parents[node]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        mp = {}
        for e in edges:
            if e[0] in mp:
                mp[e[0]].append(e[1])
            else:
                mp[e[0]] = [e[1]]
            if e[1] in mp:
                mp[e[1]].append(e[0])
            else:
                mp[e[1]] = [e[0]]

        def dfs(leaf, root):
            if leaf == root:
                return 0
            mx = 0
            for node in mp[leaf]:
                if node != root:
                    mx = max(mx, dfs(node, leaf) + 1)
                    if mx > mn:
                        return mx
            return mx

        ans = [0]

        mn = p = sys.maxsize
        for k, v in mp.items():
            mn = dfs(k, -1)
            print(k, mn)
            if mn < p:
                ans = [k]
                p = mn
            elif mn == p:
                ans.append(k)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
