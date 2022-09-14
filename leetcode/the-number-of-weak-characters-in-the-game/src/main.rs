struct Solution();

impl Solution {
    pub fn number_of_weak_characters(mut properties: Vec<Vec<i32>>) -> i32 {
        properties.sort_unstable_by_key(|key| (key[0], -key[1]));

        let mut ans = 0;
        let mut min = i32::min_value();
        for i in (0..properties.len()).rev() {
            if properties[i][1] < min {
                ans += 1;
            }
            min = min.max(properties[i][1]);
        }
        ans
    }
}

fn main() {
    assert_eq!(Solution::number_of_weak_characters(vec![vec![1,1],vec![2,1],vec![2,2],vec![1,2]]), 1);
    assert_eq!(Solution::number_of_weak_characters(vec![vec![2,2], vec![3,3]]), 1);
    println!("Hello, world!");
}
