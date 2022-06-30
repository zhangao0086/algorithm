struct Solution();

impl Solution {
    pub fn min_moves2(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        
        let median = nums[nums.len() / 2];
        nums.into_iter().fold(0, |accum, num| {
            accum + (num - median).abs()
        })
    }
}

fn main() {
    // assert_eq!(Solution::min_moves2(vec![1,2,3]), 2);
    assert_eq!(Solution::min_moves2(vec![1,10,2,9]), 16);
}