use std::vec;

struct Solution;

impl Solution {
    pub fn find_k_distant_indices(nums: Vec<i32>, key: i32, k: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        for i in 0..nums.len() {
            let mut a: i32 = -1;
            for j in 0..nums.len() {
                let distant = ((i as i32) - (j as i32)).abs();
                if distant <= k && nums[j] == key {
                    a = i as i32;
                }
                if distant <= k && nums[j] == key {
                    a = i as i32;
                }
            }
            if a != -1 {
                ans.push(a);
            }
        }
        ans
    }
}

fn main() {
    assert_eq!(Solution::find_k_distant_indices(vec![3,4,9,1,3,9,5], 9, 1), vec![1,2,3,4,5,6]);
}
