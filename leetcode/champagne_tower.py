#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        flow_table = [[0] * x for x in range(1, 101)]
        flow_table[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                remain = (flow_table[i][j] - 1) / 2
                if remain > 0:
                    flow_table[i+1][j] += remain
                    flow_table[i+1][j+1] += remain

        return min(1, flow_table[query_row][query_glass])
    
if __name__ == '__main__':
    print(Solution().champagneTower(0, 0, 0))