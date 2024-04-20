struct Solution;

impl Solution {
    pub fn find_farmland(mut land: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut res = vec![];
        let n = land.len();
        let m = land[0].len();
        for i in 0..n {
            for j in 0..m {
                if land[i][j] == 1 {
                    let mut x = i;
                    let mut y = j;
                    while x < n && land[x][j] == 1 {
                        x += 1;
                    }
                    while y < m && land[i][y] == 1 {
                        y += 1;
                    }
                    res.push(vec![i as i32, j as i32, x as i32 - 1, y as i32 - 1]);
                    for a in i..x {
                        for b in j..y {
                            land[a][b] = 0;
                        }
                    }
                }
            }
        }
        res
    }
}

fn main() {
    assert_eq!(Solution::find_farmland(
        vec![vec![1,0,0], vec![0,1,1], vec![0,1,1]]
    ), vec![vec![0,0,0,0], vec![1,1,2,2]]);
}
