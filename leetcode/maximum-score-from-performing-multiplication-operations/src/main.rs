struct Solution();

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, multipliers: Vec<i32>) -> i32 {
        let (n, m) = (nums.len(), multipliers.len());
        let mut dp = vec![vec![0; m + 1]; m + 1];

        for op in (0..m).rev() {
            for left in (0..=op).rev() {
                dp[op][left] = (
                    multipliers[op] * nums[left] + dp[op+1][left+1]).max(
                    multipliers[op] * nums[n-1-(op-left)] + dp[op+1][left]
                );
            }
        }
        dp[0][0]
    }
}

fn main() {
    assert_eq!(Solution::maximum_score(vec![1,2,3], vec![3,2,1]), 14);
    assert_eq!(Solution::maximum_score(vec![-5,-3,-3,-2,7,1], vec![-10,-5,3,4,6]), 102);
}
