use std::cmp::{min,max};

struct Solution;

impl Solution {
    pub fn max_value_of_coins(piles: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = vec![vec![0; k + 1]; piles.len() + 1];
        for i in 1..dp.len() {
            for j in 1..k + 1 {
                let mut s = 0;
                for l in 0..min(j + 1, piles[i - 1].len() + 1) {
                    dp[i][j] = max(dp[i][j], s + dp[i - 1][j - l]);
                    if l < piles[i - 1].len() {
                        s += piles[i - 1][l];
                    }
                }
            }
        }

        return dp[piles.len()][k];
    }
}

fn main() {
    assert_eq!(Solution::max_value_of_coins(vec![vec![1,100,3], vec![7,8,9]], 2), 101);
}
