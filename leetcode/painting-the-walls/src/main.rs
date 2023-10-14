struct Solution;

impl Solution {
    pub fn paint_walls(cost: Vec<i32>, time: Vec<i32>) -> i32 {
        let mut dp = vec![vec![-1; cost.len() * 2 + 1]; cost.len() + 1];
        Self::dfs(0, cost.len(), &cost, &time, &mut dp)
    }

    fn dfs(i: usize, skip: usize, cost: &[i32], time: &[i32], dp: &mut [Vec<i32>]) -> i32 {
        if cost.len() * 2 - i <= skip {
            return 0;
        }

        if i == cost.len() {
            return 1_000_000_000;
        }

        if dp[i][skip] == -1 {
            dp[i][skip] = Self::dfs(i + 1, skip - 1, cost, time, dp).min(
                cost[i] + Self::dfs(i + 1, skip + time[i] as usize, cost, time, dp)
            );
        }
        dp[i][skip]
    }
}

fn main() {
    assert_eq!(Solution::paint_walls(vec![1,2,3,2], vec![1,2,3,2]), 3);
}
