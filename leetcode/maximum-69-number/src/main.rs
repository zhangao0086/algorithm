struct Solution();

impl Solution {
    pub fn maximum69_number (num: i32) -> i32 {
        let (mut first_six, mut digit, mut copy) = (-1, 1, num);
        while copy > 0 {
            if copy % 10 == 6 {
                first_six = digit;
            }
            copy /= 10;
            digit *= 10;
        }
        if first_six == -1 { num } else { num + first_six * 3 }
    }
}
fn main() {
    assert_eq!(Solution::maximum69_number(696), 996);
    assert_eq!(Solution::maximum69_number(9), 9);
    assert_eq!(Solution::maximum69_number(6), 9);
    assert_eq!(Solution::maximum69_number(9669), 9969);
    assert_eq!(Solution::maximum69_number(9996), 9999);
    assert_eq!(Solution::maximum69_number(9999), 9999);
}
