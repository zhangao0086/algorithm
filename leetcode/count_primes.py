#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n ** 0.5 + 1)):
            if primes[i] == 1:
                primes[i*i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

            # for j in range(i * i, n, i):
            #     primes[j] = 0

        return sum(primes)

if __name__ == '__main__':
    assert Solution().countPrimes(10) == 4
    assert Solution().countPrimes(11) == 4
    assert Solution().countPrimes(12) == 5
    assert Solution().countPrimes(0) == 0
    assert Solution().countPrimes(1) == 0
    assert Solution().countPrimes(2) == 0
    assert Solution().countPrimes(3) == 1