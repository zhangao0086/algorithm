struct  Solution;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let number = nums.iter().fold(0, | acm, &n | acm ^ n);
        let (mut ans_1, mut ans_2) = (0, 0);

        let mask = number & (-number);

        for num in nums {
            if num & mask == 0 {
                ans_1 ^= num;
            } else {
                ans_2 ^= num;
            }
        }

        vec![ans_1, ans_2]
    }
}

fn main() {
    Solution::single_number(vec![1,2,1,3,2,5]);
}
