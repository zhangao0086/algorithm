#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    curr = intervals[0]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= curr[1]:
            if curr[1] < interval[1]:
                curr = curr[0], interval[1]
        else:
            yield curr
            curr = interval
    yield curr

if __name__ == '__main__':
    for i in merge_intervals([[1,12],[2,3],[4,7]]):
        i

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')
