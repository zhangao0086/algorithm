class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_numbers(prefix, n):
            count = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                count += min(n - current + 1, next_prefix - current)
                current *= 10
                next_prefix *= 10
            return count
        
        def find_kth_number(k, n):
            current = 1
            k -= 1
            while k > 0:
                count = count_numbers(current, n)
                if k >= count:
                    k -= count
                    current += 1
                else:
                    k -= 1
                    current *= 10
            return current
        
        return find_kth_number(k, n)
        


if __name__ == "__main__":
    s = Solution()
    # print(s.findKthNumber(13, 1))
    # print(s.findKthNumber(13, 2))
    # print(s.findKthNumber(13, 3))
    print(s.findKthNumber(13, 4))
    print(s.findKthNumber(13, 5))
    print(s.findKthNumber(13, 6))
    print(s.findKthNumber(13, 7))
    print(s.findKthNumber(13, 8))
    print(s.findKthNumber(13, 9))
    print(s.findKthNumber(13, 10))
    print(s.findKthNumber(13, 11))
    print(s.findKthNumber(13, 12))
    print(s.findKthNumber(13, 13))