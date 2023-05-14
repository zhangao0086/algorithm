struct Solution;

impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i32 {
        let mut dp = vec![-1; 1 << nums.len()];
        Self::dfs(&nums, 0, &mut dp)
    }

    fn dfs(nums: &Vec<i32>, mask: usize, dp: &mut Vec<i32>) -> i32 {
        if dp[mask] != -1 { return dp[mask] }

        let mut k = nums.len();
        for i in 0 .. nums.len() {
            if mask & 1 << i != 0 { k -= 1; }
        }
        k >>= 1;
        if k == 0 { return 0 } 

        dp[mask] = 0;
        for i in 0 .. nums.len() {
            for j in i + 1 .. nums.len() {
                if mask & 1 << i != 0 || mask & 1 << j != 0 { continue }
                let mask_new = mask | 1 << i | 1 << j;
                dp[mask] = dp[mask].max(k as i32 * Self::gcd(nums[i], nums[j]) + Self::dfs(nums, mask_new, dp));
            }
        }
        
        dp[mask]
    }

    fn gcd(a: i32, b: i32) -> i32 {
        if a < b { return Self::gcd(b, a); }
        if a % b == 0 { return b }
        Self::gcd(b, a % b)
    } 

}

fn main() {
    assert_eq!(Solution::max_score(vec![1,2]), 1);
    assert_eq!(Solution::max_score(vec![3,4,6,8]), 11);
    assert_eq!(Solution::max_score(vec![1,2,3,4,5,6]), 14);
}
