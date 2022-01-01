#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]


def longest_palindrome_string(s: str) -> str:
    filled = '#' + '#'.join(s) + '#'
    filled_length = len(filled)

    max_right = 0
    max_right_index = 0

    max_index = 0
    nums = [0] * filled_length

    for index in range(0, filled_length):
        skip = False

        if index < max_right:
            length = nums[2 * max_right_index - index]
            if length + index > max_right:
                nums[index] = max_right - index
            else:
                nums[index] = length
                skip = length + index < max_right
        
        if not skip:
            while index - nums[index] - 1 >= 0 and index + nums[index] + 1 < filled_length:
                if filled[index - nums[index] - 1] != filled[index + nums[index] + 1]:
                    break

                nums[index] += 1

            max_right = index + nums[index]
            max_right_index = index

        max_index = max_index if nums[max_index] >= nums[index] else index
    
    low = (max_index - nums[max_index]) // 2
    high = (max_index + nums[max_index]) // 2
    return s[low:high]

if __name__ == '__main__':
    print(Solution().longestPalindrome("aaba"))
    print(longest_palindrome_string("babadada"))
    # print(longest_palindrome_string("adaelele"))
    print(longest_palindrome_string("cabadabae"))
    print(longest_palindrome_string("aaaabcdefgfedcbaa"))
    print(longest_palindrome_string("aaba"))
    print(longest_palindrome_string("aaaaaaaaa"))