#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:

    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows < 2:
            return s

        cycle_length = 2 * numRows - 2
        result, index = [None] * length, 0
        for row in range(0, numRows, 1):
            location = row
            step_reverse = False
            while location < length:
                result[index] = s[location]
                index += 1

                if row == 0 or row == numRows - 1:
                    location += cycle_length
                else:
                    step_reverse = not step_reverse
                    location += cycle_length - 2 * row if step_reverse else 2 * row

        return "".join(result)


if __name__ == '__main__':
    print(Solution().convert('PAYPALISHIRING', 3))
