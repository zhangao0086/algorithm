struct Solution;
impl Solution {
    pub fn asteroids_destroyed(mass: i32, mut asteroids: Vec<i32>) -> bool {
        asteroids.sort_unstable();

        let mut mass = mass as i64;
        for asteroid in asteroids {
            if asteroid as i64 > mass {
                return false;
            } else {
                mass += asteroid as i64;
            }
        }
        true
    }
}

fn main() {
    assert_eq!(Solution::asteroids_destroyed(10, vec![3,9,19,5,21]), true);
}
