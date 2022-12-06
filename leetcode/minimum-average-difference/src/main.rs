struct Solution;

impl Solution {
    pub fn minimum_average_difference(nums: Vec<i32>) -> i32 {
        let (mut ans, mut min_diff) = (0, i64::MAX);
        let total_sum = nums.iter().map(|&x| x as i64).sum::<i64>();
        
        let mut prefix_sum: i64 = 0;
        for i in 0..nums.len() {
            prefix_sum += nums[i] as i64;
            let prefix_avg = prefix_sum / (i + 1) as i64;
            
            let mut suffix_avg = total_sum - prefix_sum;
            if i != nums.len() - 1 {
                suffix_avg /= (nums.len() - i - 1) as i64;
            }

            let diff = (prefix_avg - suffix_avg).abs();
            if diff < min_diff {
                ans = i as i32;
                min_diff = diff;
            }
        }
        ans
    }
}

fn main() {
    assert_eq!(Solution::minimum_average_difference(vec![2,5,3,9,5,3]), 3);
    assert_eq!(Solution::minimum_average_difference(vec![0]), 0);
    assert_eq!(Solution::minimum_average_difference(vec![0,1,0,1,0,1]), 0);
    assert_eq!(Solution::minimum_average_difference(vec![4,2,0]), 2);
}
