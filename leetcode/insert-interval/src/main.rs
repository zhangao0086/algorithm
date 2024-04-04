struct Solution;

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut new_interval = new_interval;
        let mut ans = intervals.iter().fold(vec![], |mut acc, interval| {
            if interval[1] < new_interval[0] {
                acc.push(interval.clone());
            } else if interval[0] > new_interval[1] {
                acc.push(new_interval.clone());
                new_interval = interval.clone();
            } else {
                new_interval[0] = new_interval[0].min(interval[0]);
                new_interval[1] = new_interval[1].max(interval[1]);
            }
            acc
        });

        ans.push(new_interval);
        ans
    }
}

fn main() {
    let ans = Solution::insert(vec![vec![1,3], vec![6,9]], vec![2,5]);
    println!("{:?}", ans);

    let ans = Solution::insert(vec![vec![1,2],vec![3,5],vec![6,7],vec![8,10],vec![12,16]], vec![4,8]);
    println!("{:?}", ans);

    let ans = Solution::insert(vec![], vec![5,7]);
    println!("{:?}", ans);

    let ans = Solution::insert(vec![vec![1, 5]], vec![2, 3]);
    println!("{:?}", ans);
}
