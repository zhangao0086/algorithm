struct Solution();

impl Solution {
    
    // TLE
    // pub fn is_possible(target: Vec<i32>) -> bool {
    //     let mut stack = vec![vec![1; target.len()]];

    //     while let Some(arr) = stack.pop() {
    //         if target == arr { return true; }
            
    //         let sum: i32 = arr.iter().sum();
    //         for i in 0..target.len() {
    //             if sum <=target[i] {
    //                 let mut new_arr = arr.clone();
    //                 new_arr[i] = sum;
    //                 stack.push(new_arr)
    //             }
    //         }
    //     }
    //     false
    // }

    pub fn is_possible(target: Vec<i32>) -> bool {
        use std::collections::BinaryHeap;
        let mut queue: BinaryHeap<i32> = BinaryHeap::new();
        let mut sum: i32 = target.iter().sum();
        target.iter().for_each(|item| queue.push(*item));

        while let Some(mut num) = queue.pop() {
            if num == 1 { return true; }
            sum -= num;

            if num <= sum || sum < 1 { return false; }

            num %= sum;
            sum += num;

            queue.push(if num > 0 { num } else { sum })
        }
        
        true
    }

}

fn main() {
    assert!(Solution::is_possible(vec![1,1000000000]) == true);
    assert!(Solution::is_possible(vec![1,1]) == true);
    assert!(Solution::is_possible(vec![9,3,5]) == true);
    assert!(Solution::is_possible(vec![1,1,1,2]) == false);
    assert!(Solution::is_possible(vec![8,5]) == true);
}
