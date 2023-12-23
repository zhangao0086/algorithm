struct Solution;

impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        use std::collections::HashSet;
        let mut visited = HashSet::new();
        let (mut x, mut y) = (0, 0);
        visited.insert((x, y));
        for c in path.chars() {
            match c {
                'N' => y += 1,
                'S' => y -= 1,
                'E' => x += 1,
                'W' => x -= 1,
                _ => unreachable!(),
            }
            if !visited.insert((x, y)) {
                return true;
            }
        }
        false
    }
}

fn main() {
    println!("Hello, world!");
}
