from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"{self.val}"

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 计算链表长度
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # 计算每部分的基本长度和余数
        base_size, remainder = divmod(length, k)
        
        result = []
        curr = head
        for i in range(k):
            result.append(curr)
            
            # 计算当前部分的大小
            size = base_size + (1 if i < remainder else 0)
            
            # 移动到下一部分的起始位置
            for _ in range(size - 1):
                if curr:
                    curr = curr.next
            
            # 断开链接
            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node
        
        return result

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3)))
    k = 5
    excepted = [1, 2, 3, None, None]
    res = Solution().splitListToParts(head, k)
    assert res == excepted