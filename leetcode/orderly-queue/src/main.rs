struct Solution;
impl Solution {
    pub fn orderly_queue(s: String, k: i32) -> String {
        let mut v = s.chars().collect::<Vec<char>>();
        if k > 1 {
            v.sort();
            v.iter().collect()
        } else {
            let mut ans = v.clone();
            for _ in 0..v.len() {
                v.rotate_left(1);
                if ans > v {
                    ans = v.clone();
                }
            }
            ans.iter().collect()
        }
    }
}

fn main() {
    assert_eq!(Solution::orderly_queue("cba".to_string(), 1), "acb");
    assert_eq!(Solution::orderly_queue("baaca".to_string(), 3), "aaabc");
}
