struct Solution;

impl Solution {
    pub fn find_error_nums(mut nums: Vec<i32>) -> Vec<i32> {
        let (mut dup, mut missing) = (-1, -1);
        for i in 0..nums.len() {
            let index = nums[i].abs()-1;
            if nums[index as usize] < 0 { 
                dup = nums[i].abs();
            } else {
                nums[index as usize] = nums[index as usize]*-1;
            }
        }
        for i in 0..nums.len() {
            if nums[i] > 0 {
                missing = (i+1) as i32;
                break;
            }
        }
        vec![dup, missing]
    }
}

fn main() {
    assert_eq!(Solution::find_error_nums(vec![2,3,2]), vec![2,1]);
    assert_eq!(Solution::find_error_nums(vec![3,2,2]), vec![2,1]);
    assert_eq!(Solution::find_error_nums(vec![1,2,2,4]), vec![2,3]);
    assert_eq!(Solution::find_error_nums(vec![1,1]), vec![1,2]);
}
