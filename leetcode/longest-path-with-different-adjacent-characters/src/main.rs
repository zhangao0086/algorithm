struct Solution;

impl Solution {
    pub fn longest_path(parent: Vec<i32>, s: String) -> i32 {
        let mut ans = 0;
        let mut tree = vec![vec![]; parent.len()];
        for i in 1..parent.len() {
            tree[parent[i] as usize].push(i);
        }
        Solution::def(0, &tree, &s.chars().collect(), &mut ans);
        ans
    }

    fn def(node: usize, tree: &Vec<Vec<usize>>, s: &Vec<char>, ans: &mut i32) -> i32 {
        let (mut max1, mut max2) = (0, 0);
        for child in &tree[node] {
            let longest_child_path = Solution::def(*child, tree, s, ans);
            if s[*child] == s[node] { continue }

            if longest_child_path > max1 {
                max2 = max1;
                max1 = longest_child_path;
            } else if longest_child_path > max2 {
                max2 = longest_child_path;
            }
        }
        
        *ans = std::cmp::max(*ans, max1 + max2 + 1);
        max1 + 1
    }
}

fn main() {
    // assert_eq!(Solution::longest_path(vec![-1,0,0,1,1,2], "abacbe".to_string()), 3);
    assert_eq!(Solution::longest_path(vec![-1,0,0,0], "aabc".to_string()), 3);
}
