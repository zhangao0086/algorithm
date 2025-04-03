from typing import List

class Solution:
    # Approach 1
    # def maximumTripletValue(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     leftMax = [0] * n
    #     rightMax = [0] * n
    #     for i in range(1, n):
    #         leftMax[i] = max(leftMax[i - 1], nums[i - 1])
    #         rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
    #     res = 0
    #     for j in range(1, n - 1):
    #         res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
    #     return res

    # Approach 2
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumTripletValue([12,6,1,2,7]))
    print(solution.maximumTripletValue([1,10,3,4,19]))
    print(solution.maximumTripletValue([1, 2, 3]))
