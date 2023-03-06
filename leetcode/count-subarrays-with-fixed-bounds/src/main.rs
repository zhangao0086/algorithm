struct Solution;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut ans = 0;
        let (mut min_position, mut max_position, mut left_bound) = (-1, -1, -1);
        for (i, &num) in nums.iter().enumerate() {
            if num < min_k || num > max_k {
                left_bound = i as i64;
            }
            
            if num == min_k {
                min_position = i as i64;
            }
            
            if num == max_k {
                max_position = i as i64;
            }

            ans += (min_position.min(max_position) - left_bound).max(0);
        }
        ans
    }
}

fn main() {
    // assert_eq!(Solution::count_subarrays(vec![1,3,5,2,7,5], 1, 5), 2);
    assert_eq!(Solution::count_subarrays(vec![1,1,1,1], 1, 1), 10);
}
