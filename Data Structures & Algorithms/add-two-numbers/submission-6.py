# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        answer = nextsum = ListNode()
        if(not l1):
            return l2
        if(not l2):
            return l1
        while(l1 or l2 or carry>0):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            added = v1+v2+carry
            lastdigit=added%10
            nextsum.val=lastdigit
            if added>=10:
                carry=1
            else:
                carry=0
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            if(carry==1 or l1 or l2):
                nextsum.next=ListNode()
            nextsum=nextsum.next
        return answer
