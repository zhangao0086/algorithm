#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from typing import List

class Solution:
    # def videoStitching(self, clips: List[List[int]], T: int) -> int:
    #     if T == 0: return 0
    #     clips.sort(key=lambda x: (x[0], x[1]))
    #     if clips[0][0] != 0: return -1
    #     ans = [clips[0]]

    #     for i in range(1, len(clips)):
    #         clip = clips[i]
    #         if ans[-1][1] >= T: break
    #         if ans[-1][0] == clip[0] and ans[-1][1] < clip[1]:
    #             ans[-1] = clip
    #         else:     
    #             if len(ans) > 1 and ans[-2][1] >= clip[0] and clip[1] >= ans[-1][1]:
    #                 ans.pop()
    #             if clip[1] > ans[-1][1]:
    #                 if clip[0] <= ans[-1][1]:
    #                     ans.append(clip)
    #                 else:
    #                     break
    #     return len(ans) if ans[-1][1] >= T else -1

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        end1, end2, ans = -1, 0, 0
        for clip in sorted(clips):
            if end2 >= T or clip[0] > end2: break
            if end1 < clip[0] <= end2:
                ans, end1 = ans + 1, end2
            end2 = max(end2, clip[1])

        return ans if end2 >= T else -1

if __name__ == '__main__':
    assert Solution().videoStitching([[0, 4], [2, 8], [5, 10], [9, 12], [8, 12]], 12) == 3
    assert Solution().videoStitching([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]], 5) == 1
    assert Solution().videoStitching([[0,1],[1,2]], 5) == -1
    assert Solution().videoStitching([[0, 4], [5, 10], [9, 12], [8, 13]], 13) == -1
    assert Solution().videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9) == 3