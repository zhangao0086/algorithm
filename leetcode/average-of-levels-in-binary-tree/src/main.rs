// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

struct Solution;

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut ans = Vec::new();
        let mut stack = vec![root];

        while !stack.is_empty() {
            let (n, mut sum) = (stack.len(), 0);
            for _ in 0..n {
                if let Some(node) = stack.remove(0) {
                    sum += i64::from(node.borrow().val);
                    if let Some(left) = node.borrow_mut().left.take() {
                        stack.push(Some(left));
                    }

                    if let Some(right) = node.borrow_mut().right.take() {
                        stack.push(Some(right));
                    }
                }
            }
            ans.push(sum as f64 / n as f64);
        }
        ans
    }
}

fn main() {
    println!("Hello, world!");
}
