class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        cur_list = final
        temp = ListNode()
        cur1 = l1
        cur2 = l2
        carry = 0
        while cur1 or cur2 or carry > 0:
            v1 = cur1 and cur1.val or 0
            v2 = cur2 and cur2.val or 0

            next_digit = v1 + v2 + carry

            carry = next_digit // 10
            next_digit %= 10
            
            cur_list.next = ListNode(next_digit)
            cur_list = cur_list.next
            cur1 = cur1 and cur1.next
            cur2 = cur2 and cur2.next
        return final.next
        