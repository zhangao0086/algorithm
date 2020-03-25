#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:

    # 解法一
    # integer_dict = {
    #     1: "I",
    #     4: "IV",
    #     5: "V",
    #     9: "IX",
    #     10: "X",
    #     40: "XL",
    #     50: "L",
    #     90: "XC",
    #     100: "C",
    #     400: "CD",
    #     500: "D",
    #     900: "CM",
    #     1000: "M",
    # }

    # def intToRoman(self, num: int) -> str:
    #     ans, carry = "", 1
    #     while num > 0:
    #         digit = num % 10 * carry
    #         num = num // 10
    #         carry *= 10
    #         if digit == 0: continue

    #         roman = Solution.integer_dict.get(digit)
    #         if roman is None:
    #             nearest, fill_count = digit, 0
    #             while nearest not in Solution.integer_dict:
    #                 nearest -= carry // 10
    #                 fill_count += 1
    #             if nearest * (fill_count + 1) == digit:
    #                 ans = Solution.integer_dict[nearest] * (fill_count + 1) + ans
    #             else:
    #                 ans = Solution.integer_dict[nearest] + Solution.integer_dict[nearest - 4 * carry // 10] * fill_count + ans
    #         else:
    #             ans = roman + ans

    #     return ans

    # 解法二
    # integer_mapper = [
    #     (1000, "M"),
    #     (900, "CM"),
    #     (500, "D"),
    #     (400, "CD"),
    #     (100, "C"),
    #     (90, "XC"),
    #     (50, "L"),
    #     (40, "XL"),
    #     (10, "X"),
    #     (9, "IX"),
    #     (5, "V"),
    #     (4, "IV"),
    #     (1, "I"),
    # ]

    # def intToRoman(self, num: int) -> str:
    #     ans = ""
    #     for integer, roman in Solution.integer_mapper:
    #         ans += (num // integer) * roman
    #         num %= integer

    #         if num == 0: break
    #     return ans

    # 解法三，采用解法二的表
    # def intToRoman(self, num: int) -> str:
    #     ans = ""
    #     for integer, roman in Solution.integer_mapper:
    #         while num >= integer:
    #             ans += roman
    #             num -= integer
    #         if num == 0: break

    #     return ans
    
    # 解法四
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    def intToRoman(self, num: int) -> str:
        return Solution.M[num // 1000] + Solution.C[num % 1000 // 100] + Solution.X[num % 100 // 10] + Solution.I[num % 10]
    
if __name__ == '__main__':
    print(Solution().intToRoman(100))
    print(Solution().intToRoman(10))
    print(Solution().intToRoman(1))
    print(Solution().intToRoman(3))
    print(Solution().intToRoman(4))
    print(Solution().intToRoman(9))
    print(Solution().intToRoman(19))
    print(Solution().intToRoman(28))
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(1994))
    print(Solution().intToRoman(3999))