#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

import collections

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        visited = [False] * 10
        visited[0] = True
        consecutive_nodes = collections.defaultdict(dict)
        consecutive_nodes[1][9] = consecutive_nodes[9][1] = 5
        consecutive_nodes[2][8] = consecutive_nodes[8][2] = 5
        consecutive_nodes[3][7] = consecutive_nodes[7][3] = 5
        consecutive_nodes[4][6] = consecutive_nodes[6][4] = 5
        consecutive_nodes[1][3] = consecutive_nodes[3][1] = 2
        consecutive_nodes[7][9] = consecutive_nodes[9][7] = 8
        consecutive_nodes[1][7] = consecutive_nodes[7][1] = 4
        consecutive_nodes[3][9] = consecutive_nodes[9][3] = 6

        def consecutive_node(i, j) -> int:
            if i in consecutive_nodes and j in consecutive_nodes[i]:
                return consecutive_nodes[i][j]
            else:
                return 0

        def dfs(steps, num) -> int:
            count = 0
            if steps >= m: count += 1
            if steps + 1 > n: return steps
            visited[num] = True
            for i in range(1, 10):
                if visited[i] == False and visited[consecutive_node(num, i)]:
                    count += dfs(steps + 1, i)

            visited[num] = False
            return count

        return dfs(1, 1) * 4 + dfs(1, 2) * 4 + dfs(1, 5)

if __name__ == '__main__':
    print(Solution().numberOfPatterns(1, 1))
    print(Solution().numberOfPatterns(1, 2))
    print(Solution().numberOfPatterns(3, 4))