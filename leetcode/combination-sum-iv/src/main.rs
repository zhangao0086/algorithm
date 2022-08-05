struct Solution();

impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let target = target as usize;
        let mut dp = vec![0; target + 1];
        dp[0] = 1;

        for i in 1..=target {
            for num in nums.iter() {
                let num = *num as usize;
                if i >= num {
                    dp[i] += dp[i - num]
                }
            }
        }

        dp[target]
    }
}

fn main() {
    assert_eq!(Solution::combination_sum4(vec![2,3], 4), 1);
    assert_eq!(Solution::combination_sum4(vec![1,2,3], 4), 7);
}
