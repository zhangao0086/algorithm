struct Solution;

impl Solution {
    pub fn knight_probability(n: i32, k: i32, row: i32, column: i32) -> f64 {
        let mut dp = vec![vec![vec![0.0; n as usize]; n as usize]; k as usize + 1];
        let directions = vec![
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ];
        dp[0][row as usize][column as usize] = 1.0;
        for step in 1..=k as usize {
            for i in 0..n as usize {
                for j in 0..n as usize {
                    for direction in &directions {
                        let x = i as i32 + direction.0;
                        let y = j as i32 + direction.1;
                        if x >= 0 && x < n && y >= 0 && y < n {
                            dp[step][i][j] += dp[step - 1][x as usize][y as usize] / 8.0;
                        }
                    }
                }
            }
        }
        let mut res = 0.0;
        for i in 0..n as usize {
            for j in 0..n as usize {
                res += dp[k as usize][i][j];
            }
        }
        res
    }
}

fn main() {
    let n = 3;
    let k = 2;
    let row = 0;
    let column = 0;
    let res = Solution::knight_probability(n, k, row, column);
    println!("{}", res);
}
