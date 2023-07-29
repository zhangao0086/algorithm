use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n > 4800 {
            1.
        } else {
            Self::dfs(n, n, &mut HashMap::new())
        }
    }

    pub fn dfs(a: i32, b: i32, dp: &mut HashMap<(i32, i32), f64>) -> f64 {
        if let Some(&v) = dp.get(&(a, b)) {
            return v;
        }

        match (a <= 0, b <= 0) {
            (true, true) => 0.5,
            (false, true) => 0.,
            (true, false) => 1.,
            _ => {
                let result = (
                    Self::dfs(a - 100, b, dp) +
                    Self::dfs(a - 75, b - 25, dp) +
                    Self::dfs(a - 50, b - 50, dp) + 
                    Self::dfs(a - 25, b - 75, dp)
                ) / 4.0;
                dp.insert((a, b), result);
                result
            }
        }
    }
}
fn main() {
    assert_eq!(Solution::soup_servings(50), 0.625);
    assert_eq!(Solution::soup_servings(100), 0.71875);
}
