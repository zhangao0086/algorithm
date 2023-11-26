struct Solution;

impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let mut matrix = matrix;
        let (m, n) = (matrix.len(), matrix[0].len());
        let mut res = 0;
        for i in 1..m {
            for j in 0..n {
                if matrix[i][j] == 1 {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }
        }
        for i in 0..m {
            matrix[i].sort_unstable();
            for j in (0..n).rev() {
                res = res.max(matrix[i][j] * (n - j) as i32);
            }
        }
        res
    }
}

fn main() {
    assert_eq!(Solution::largest_submatrix(vec![
        vec![0,0,1],
        vec![1,1,1],
        vec![1,0,1],
    ]), 4);

    assert_eq!(Solution::largest_submatrix(vec![
        vec![1,0,1,0,1],
    ]), 3);
}
