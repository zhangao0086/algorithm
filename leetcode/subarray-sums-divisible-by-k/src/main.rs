struct Solution;

impl Solution {
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        let mut prefixMod = 0;
        
        let mut modGroups = vec![0; k as usize];
        modGroups[0] = 1;

        for num in nums {
            prefixMod = (prefixMod + num % k + k) % k;

            ans += modGroups[prefixMod as usize];
            modGroups[prefixMod as usize] += 1;
        }

        ans
    }
}

fn main() {
    assert_eq!(Solution::subarrays_div_by_k(vec![4,5,0,-2,-3,1], 5), 7);
    assert_eq!(Solution::subarrays_div_by_k(vec![5], 9), 0);
}
