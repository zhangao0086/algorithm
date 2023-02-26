// Definition for a binary tree node.
struct Solution;

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

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() { return 0 };

        let mut depth = 0;
        let mut queue = vec![root];
        while !queue.is_empty() {
            depth += 1;
            let mut next = vec![];
            for node in queue {
                if let Some(node) = node {
                    let node = node.borrow();
                    if node.left.is_none() && node.right.is_none() {
                        return depth;
                    }
                    next.push(node.left.clone());
                    next.push(node.right.clone());
                }
            }
            queue = next;
        }
        depth
    }
}

fn main() {
    let mut root = Some(Rc::new(RefCell::new(TreeNode::new(3))));
    root.as_mut().unwrap().borrow_mut().right = Some(Rc::new(RefCell::new(TreeNode::new(20))));
    assert_eq!(Solution::min_depth(root), 2);
}
