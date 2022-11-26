struct Solution;

impl Solution {
    pub fn job_scheduling(start_time: Vec<i32>, end_time: Vec<i32>, profit: Vec<i32>) -> i32 {
        let mut jobs = start_time
            .into_iter()
            .zip(end_time.into_iter())
            .zip(profit.into_iter())
            .map(|((start, end), profit)| (start, end, profit) )
            .collect::<Vec<_>>();
        
        jobs.sort_by_key(|job| job.1);
        
        let n = jobs.len();
        let mut dp = vec![0; n];
        dp[0] = jobs[0].2;
        for i in 1..n {
            dp[i] = jobs[i].2.max(dp[i-1]);
            for j in (0..=i-1).rev() {
                if jobs[j].1 <= jobs[i].0 {
                    dp[i] = dp[i].max(dp[j] + jobs[i].2);
                    break;
                }
            }
        }

        dp.iter().max().unwrap().clone()
    }
}

fn main() {
    assert_eq!(Solution::job_scheduling(vec![1,2,3,4,6], vec![3,5,10,6,9], vec![20,20,100,70,60]), 150);
}
