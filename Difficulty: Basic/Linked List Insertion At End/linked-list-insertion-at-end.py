class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        if head is None:
            head = Node(x)
            return head
            
        curr  = head
        while curr.next:
            curr = curr.next
            
        curr.next = Node(x)
        
        return head