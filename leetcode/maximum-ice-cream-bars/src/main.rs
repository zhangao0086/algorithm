struct Solution;

impl Solution {
    pub fn max_ice_cream(mut costs: Vec<i32>, coins: i32) -> i32 {
        costs.sort_unstable();
        let mut sum = 0;
        for i in 0..costs.len(){
            if sum + costs[i] > coins {
                return i as i32;
            }
            sum += costs[i];
        }
        costs.len() as i32
    }
}

fn main() {
    assert_eq!(Solution::max_ice_cream(vec![1,3,2,4,1], 7), 4)
}
