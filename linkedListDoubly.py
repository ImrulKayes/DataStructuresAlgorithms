###creating a linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev=None

class linkedList:
    def __init__(self):
        self.head=ListNode(0)
        self.tail=ListNode(0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def insert(self,data):
        curr=self.head
        while curr.next!=self.tail:
            curr=curr.next
        newNode=ListNode(data)
        curr.next=newNode
        newNode.prev=curr
        newNode.next=self.tail
        self.tail.prev=newNode

    def delete(self,val):
        if self.head==self.tail:
            return
        curr=self.head.next
        
        while curr.val!=val:
            curr=curr.next
        prevNode=curr.prev
        nextNode=curr.next
        prevNode.next=nextNode
        nextNode.prev=prevNode
        

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail
    
    def printList(self,head):
        if head==self.tail:
            return
        else:
            curr=head.next
        while curr!=self.tail:
            print curr.val
            curr=curr.next
            

l=linkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)

l.delete(1)
head=l.getHead()
l.printList(head)
