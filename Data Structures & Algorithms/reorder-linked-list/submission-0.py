# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        one=head
        half=head
        while(one and one.next!=None and one.next.next!=None):
            one=one.next.next
            half=half.next
        newtemp=half.next
        half.next=None
        prev,curr=None,newtemp
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        last=head
        while(head and prev):
            temp1=head.next
            temp2=prev.next
            head.next=prev
            prev.next=temp1
            head=temp1
            prev=temp2
        


            

