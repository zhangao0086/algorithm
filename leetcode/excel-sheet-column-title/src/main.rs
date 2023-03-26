struct Solution;

impl Solution {
    pub fn convert_to_title(mut column_number: i32) -> String {
        let mut result: Vec<u8> = Vec::new();
        while column_number > 0 {
            column_number -= 1;
            result.push(65 + (column_number % 26) as u8);
            column_number /= 26;
        }
        result.reverse();
        String::from_utf8(result).unwrap()
    }
}

fn main() {
    assert_eq!(Solution::convert_to_title(1), "A");
    assert_eq!(Solution::convert_to_title(28), "AB");
    assert_eq!(Solution::convert_to_title(701), "ZY");
}
