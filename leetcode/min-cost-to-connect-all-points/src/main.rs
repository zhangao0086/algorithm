struct Solution;

impl Solution {
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let points = points.into_iter().map(|p| (p[0], p[1])).collect::<Vec<_>>();

        let mut connected = vec![false; points.len()];
        let mut dist = vec![i32::MAX; points.len()];

        let mut min_idx = 0;
        let mut min_cost = 0;

        let mut total_cost = 0;

        for _ in 0..points.len() {
            connected[min_idx] = true;
            total_cost += min_cost;

            let cur_point = points[min_idx];
            min_cost = i32::MAX;

            for (idx, point) in points.iter().enumerate() {
                if !connected[idx] {
                    dist[idx] = dist[idx]
                        .min((cur_point.0 - point.0).abs() + (cur_point.1 - point.1).abs());
                    if dist[idx] < min_cost {
                        min_cost = dist[idx];
                        min_idx = idx;
                    }
                }
            }
        }

        total_cost
    }
}

fn main() {
    let cost = Solution::min_cost_connect_points(vec![vec![0,0], vec![2,2], vec![3,10], vec![5,2], vec![7,0]]);
    println!("{:?}", cost);
}
