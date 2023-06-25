struct Solution;

impl Solution {
    pub fn num_sub(s: String) -> i32 {
        const MODULO: i64 = 10_i64.pow(9) + 7;
        let (mut count, mut result) = (0, 0);
        for c in s.chars() {
            if c == '1' {
                count += 1;
            } else {
                result += count * (count + 1) / 2;
                count = 0;
            }
        }
        result += count * (count + 1) / 2;
        (result % MODULO) as i32
    }
}
fn main() {
    assert_eq!(Solution::num_sub(String::from("0110111")), 9);
}
