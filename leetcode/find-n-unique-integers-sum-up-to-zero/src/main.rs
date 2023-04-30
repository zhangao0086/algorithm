struct Solution;

impl Solution {
    pub fn sum_zero(n: i32) -> Vec<i32> {
        let mut result = vec![];
        if n % 2 == 1 {
            result.push(0);
        }
        for i in 1..=n / 2 {
            result.push(i);
            result.push(-i);
        }
        result
    }
}
fn main() {
    assert_eq!(Solution::sum_zero(5), vec![-7,-1,1,3,4]);
}
