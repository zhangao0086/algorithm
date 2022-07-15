struct Solution();

impl Solution {
    pub fn max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {
        let mut max_area = 0;
        let (m, n) = (grid.len(), grid[0].len());
        let mut seen = vec![vec![false; n]; m];

        for i in 0..m {
            for j in 0..n {
                if seen[i][j] || grid[i][j] == 0 { continue; }
                seen[i][j] = true;

                let mut area = 0;
                let mut stack = vec![(i, j)];

                while let Some((x, y)) = stack.pop() {
                    area += 1;

                    for (dx, dy) in [(x+1, y), (((x as isize)-1) as usize, y), (x, y+1), (x, ((y as isize)-1) as usize)] {
                        if dx < m && dy < n && grid[dx][dy] == 1 && !seen[dx][dy] {
                            stack.push((dx, dy));
                            seen[dx][dy] = true;
                        }
                    }
                }
                max_area = max_area.max(area);
            }
        }
        
        max_area
    }
}

fn main() {
    assert_eq!(
        Solution::max_area_of_island(
        vec![
            vec![0,0,1,0,0,0,0,1,0,0,0,0,0],
            vec![0,0,0,0,0,0,0,1,1,1,0,0,0],
            vec![0,1,1,0,1,0,0,0,0,0,0,0,0],
            vec![0,1,0,0,1,1,0,0,1,0,1,0,0],
            vec![0,1,0,0,1,1,0,0,1,1,1,0,0],
            vec![0,0,0,0,0,0,0,0,0,0,1,0,0],
            vec![0,0,0,0,0,0,0,1,1,1,0,0,0],
            vec![0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]), 6);
    
        assert_eq!(
            Solution::max_area_of_island(
            vec![
                vec![0,0,0,0,0,0,0,0],
            ]), 0);
    
}
