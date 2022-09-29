struct Solution();

impl Solution {
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let k = k as usize;
        if arr.len() == k { return arr; } 
        let (mut left, mut right) = (0, arr.len() - k);
        
        while left < right {
            let mid = (left + right) / 2;
            if x - arr[mid] > arr[mid+k] - x {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        Vec::from(&arr[left..left+k])
    }
}

fn main() {
    println!("{:?}", Solution::find_closest_elements(vec![1,2,3,4,5], 4, -1));
}
