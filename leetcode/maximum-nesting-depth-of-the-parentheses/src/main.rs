struct Solution;

impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut max_depth = 0;
        let mut depth = 0;
        for c in s.chars() {
            match c {
                '(' => {
                    depth += 1;
                    max_depth = max_depth.max(depth);
                }
                ')' => {
                    depth -= 1;
                }
                _ => {}
            }
        }
        max_depth
    }
}

fn main() {
    assert_eq!(Solution::max_depth("(1+(2*3)+((8)/4))+1".to_string()), 3);
}
