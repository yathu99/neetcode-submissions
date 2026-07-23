"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newNode = None
        head2=head
        randomStore=dict()
        prev=None
        while(head):
            newNode=Node(head.val)
            randomStore[head]=newNode
            if(prev):
                prev.next=newNode
            prev=newNode
            head = head.next
            newNode = newNode.next
        final=res=randomStore.get(head2)
        while(head2):
            if(head2.random):
                res.random=randomStore[head2.random]
            else:
                res.random=None
            res=res.next
            head2=head2.next
        return final
        
            
            
