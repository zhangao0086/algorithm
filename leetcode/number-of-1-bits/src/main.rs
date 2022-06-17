struct Solution {} 

impl Solution {
    // pub fn hammingWeight (n: u32) -> i32 {
    //     n.count_ones() as i32
    // }

    pub fn hammingWeight (mut n: u32) -> i32 {
        let mut ans = 0;
        for _ in 0..32 {
            ans += (n & 1) as i32;
            n >>= 1;
        }
        ans
    }
}

fn main() {
    let n = 0b_00000000000000000000000000001011;
    assert!(Solution::hammingWeight(n) == 3);
}
