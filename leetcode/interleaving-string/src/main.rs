struct Solution();

impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        if s1.len() + s2.len() != s3.len() { return false; }
        let s1 = s1.as_bytes();
        let s2 = s2.as_bytes();
        let s3 = s3.as_bytes();

        // let mut dp = vec![vec![false; s2.len()+1]; s1.len()+1];
        // for i in 0..=s1.len() {
        //     for j in 0..=s2.len() {
        //         if i == 0 && j == 0 {
        //             dp[i][j] = true;
        //         } else if i == 0 {
        //             dp[i][j] = dp[i][j-1] && (s2[j-1] == s3[i+j-1]);
        //         } else if j == 0 {
        //             dp[i][j] = dp[i-1][j] && (s1[i-1] == s3[i+j-1]);
        //         } else {
        //             dp[i][j] = dp[i-1][j] && (s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && (s2[j-1] == s3[i+j-1]));
        //         }
        //     }
        // }

        // dp[s1.len()][s2.len()]

        let mut dp = vec![false; s2.len()+1];
        for i in 0..=s1.len() {
            for j in 0..=s2.len() {
                if i == 0 && j == 0 {
                    dp[j] = true;
                } else if i == 0 {
                    dp[j] = dp[j-1] && (s2[j-1] == s3[i+j-1]);
                } else if j == 0 {
                    dp[j] = dp[j] && (s1[i-1] == s3[i+j-1]);
                } else {
                    dp[j] = dp[j] && (s1[i-1] == s3[i+j-1]) || (dp[j-1] && (s2[j-1] == s3[i+j-1]));
                }
            }
        }

        dp[s2.len()]
    }
}

fn main() {
    assert_eq!(Solution::is_interleave("aabcc".to_string(), "dbbca".to_string(), "aadbbcbcac".to_string()), true);
    assert_eq!(Solution::is_interleave("aabcc".to_string(), "dbbca".to_string(), "aadbbbaccc".to_string()), false);
    assert_eq!(Solution::is_interleave("".to_string(), "".to_string(), "".to_string()), true);
    assert_eq!(Solution::is_interleave("a".to_string(), "b".to_string(), "a".to_string()), false);

    assert_eq!(Solution::is_interleave(
        "abababababababababababababababababababababababababababababababababababababababababababababababababbb".to_string(), 
        "babababababababababababababababababababababababababababababababababababababababababababababababaaaba".to_string(), 
        "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababbb".to_string()), false);
}
