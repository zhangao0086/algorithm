#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"


class Solution:

    num_map = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
        11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
        15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
        20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
        70: "Seventy", 80: "Eighty", 90: "Ninety",
    }

    carry_map = {
        100: "Hundred",
        1000: "Thousand",
        100000: "Hundred",
        1000000: "Million",
        100000000: "Hundred",
        1000000000: "Billion",
    }

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        result = None
        carry = 1

        while num > 0:
            num_bit = num % 1000

            if num_bit > 0:
                high = int(num_bit / 100)
                low_digits = num_bit % 100
                if low_digits < 20:
                    middle = low = 0
                else:
                    middle = int(num_bit / 10) % 10
                    low = num_bit % 10
                    low_digits = 0
                low_carry = Solution.carry_map.get(carry)

                for word in [
                    None if low_carry is None else low_carry,
                    None if low_digits == 0 else Solution.num_map.get(low_digits),
                    None if low == 0 else Solution.num_map.get(low),
                    None if middle == 0 else Solution.num_map.get(middle * 10),
                    None if high == 0 else Solution.num_map.get(high) + " " + Solution.carry_map.get(carry * 100),
                ]:
                    if word is not None:
                        result = word + ("" if result is None else (" " + result))

            num = int(num / 1000)
            carry *= 1000

        return result


if __name__ == '__main__':
    print(Solution().numberToWords(111321))
