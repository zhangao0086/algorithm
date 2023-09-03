struct Solution;

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let mut current = vec![1; n as usize];
        for _ in 1..m {
            for j in 1..n as usize {
                current[j] += current[j - 1];
            }
        }
        current[n as usize - 1]
    }
}

fn main() {
    println!("Hello, world!");
}
