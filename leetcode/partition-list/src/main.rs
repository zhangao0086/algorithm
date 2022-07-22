struct Solution();

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

impl Solution {
    pub fn partition(mut head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let (mut left_head, mut right_head) = (ListNode::new(0), ListNode::new(0));
        let (mut left, mut right) = (&mut left_head, &mut right_head);

        while let Some(mut node) = head {
            head = node.next.take();
            if node.val < x {
                left.next = Some(node);
                left = left.next.as_mut().unwrap();
            } else {
                right.next = Some(node);
                right = right.next.as_mut().unwrap();
            }
        }

        left.next = right_head.next;
        left_head.next
    }
}

fn main() {
    let v = vec![1,4,3,2,5,2];
    let mut head = ListNode::new(0);
    let mut p = &mut head;
    for value in v {
        let node = ListNode::new(value);
        p.next = Some(Box::new(node));
        p = p.next.as_mut().unwrap();
    }

    let ans = Solution::partition(head.next, 3);
    print!("{:?}", ans);
}
