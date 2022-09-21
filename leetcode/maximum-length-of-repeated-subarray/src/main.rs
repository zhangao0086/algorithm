struct Solution();

impl Solution {
    pub fn find_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (mut dp, mut pre_dp) = (vec![0; nums2.len()+1], vec![0; nums2.len()+1]);
        let mut ans = 0;

        for i in 1..=nums1.len() {
            for j in 1..=nums2.len() {
                dp[j] = if nums1[i-1] == nums2[j-1] { pre_dp[j-1]+1 } else { 0 };
                ans = ans.max(dp[j]);
            }
            // (pre_dp, dp) = (dp, pre_dp);
            std::mem::swap(&mut pre_dp, &mut dp);
        }
        ans
    }
}

fn main() {
    assert_eq!(Solution::find_length(vec![1,0,0,0,1,0,0,1,0,0], vec![0,1,1,1,0,1,1,1,0,0]), 3);
    assert_eq!(Solution::find_length(vec![1,2,3,2,1], vec![3,2,1,4,7]), 3);
}
