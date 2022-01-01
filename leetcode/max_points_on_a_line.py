#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points_length = len(points)
        if points_length <= 2:
            return points_length 

        # 计算最大公约数
        def calc_gcd(x: int, y: int) -> int:
            if y == 0: return x
            return calc_gcd(y, x % y)
        
        lengths = {}
        max_points = 0
        for i in range(points_length - 1):
            lengths.clear()

            max_line = 0
            same_point = 0
            for j in range(i + 1, points_length):
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]

                gcd = calc_gcd(x, y)
                if gcd == 0:
                    same_point += 1
                    continue

                key = f"{x // gcd}-{y // gcd}"

                length = lengths.get(key, 0) + 1
                lengths[key] = length
                max_line = max(max_line, length)
            max_points = max(max_points, max_line + same_point + 1)

        return max_points

if __name__ == '__main__':
    print(Solution().maxPoints([[0,0],[0,0]]))
    print(Solution().maxPoints([[1,1]]))
    print(Solution().maxPoints([[1,1],[2,2]]))
    print(Solution().maxPoints([[1,1],[2,2],[3,3]]))
    print(Solution().maxPoints([[1,1],[2,2],[3,3],[1,1]]))
    print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))