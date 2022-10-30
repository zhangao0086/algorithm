struct Solution;

impl Solution {
    pub fn earliest_full_bloom(plant_time: Vec<i32>, grow_time: Vec<i32>) -> i32 {
        let (mut current_grow_time, mut current_plant_time) = (0, 0);
        let mut range: Vec<usize> = (0..plant_time.len()).collect();
        range.sort_by_key(|k| -grow_time[*k]);
        for i in range {
            current_plant_time = current_plant_time + plant_time[i];
            current_grow_time = current_grow_time.max(current_plant_time + grow_time[i]);
        }
        current_grow_time
    }
}
fn main() {
    assert_eq!(Solution::earliest_full_bloom(vec![1,2,3,2], vec![2,1,2,1]), 9);
}
