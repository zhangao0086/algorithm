struct Solution;

impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        let mut count = 0;
        for p in patterns {
            if word.contains(&p) {
                count += 1;
            }
        }
        count
    }
}

fn main() {
    assert_eq!(Solution::num_of_strings(vec!["a".to_string(),"abc".to_string(),"bc".to_string(),"d".to_string()], "abc".to_string()), 3);
}
