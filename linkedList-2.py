### Linked lists (ch2, cracking the coding interview)



###creating a linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class linkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if self.head==None:
            newNode=ListNode(data)
            self.head=newNode
        else:
            head=self.head
            while head.next!=None:
                head=head.next
            newNode=ListNode(data)
            head.next=newNode

    def getHead(self):
        return self.head
    def getTail(self):
        head=self.head
        while head.next!=None:
            head=head.next
        return head
    
    def printList(self,head=None):
        if head==None:
            head=self.head
        while head!=None:
            print head.val
            head=head.next
          

    def sortList(self, head):
        # apply mergesort, divide the whole list into two and merge
        
        if head==None:
            return None
        if head.next==None:
            return head
        
        mainHead=head
        count=0
        while head:
            count+=1
            head=head.next
        head=mainHead
        for i in range(int(count/2)):
            prev=head
            head=head.next
        prev.next=None
        headA=self.sortList(mainHead)
        headB=self.sortList(head)
        newHead=self.merge(headA,headB)
        return newHead
        
    def merge(self,headA,headB):
        # the concise merge version is below
        if headA==None and headB==None:
            return None
        if headA==None:
            return headB
        if headB==None:
            return headA
        # fix the head
        if headA.val<=headB.val:
            head=headA
            headA=headA.next
        else:
            head=headB
            headB=headB.next
        current=head
        
        while headA and headB:
            prev=current
            if headA.val<=headB.val:
                current=headA
                prev.next=current
                headA=headA.next
            else:
                current=headB
                prev.next=current
                headB=headB.next               
        if headA:
                current.next=headA             
        if headB:
                current.next=headB
        return head

    def merge(self, l1, l2):
            vhead = curr = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return vhead.next      

    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next


    def insertionSortList(self, head):
        # Sort a linked list using insertion sort.
        dummy=ListNode(-100)
        current=head
        while current:
            current1=dummy
            # find a postion (oldCurrent1 ) of the sorted list after which new node will be inserted
            while current1 and current1.val<current.val:
                oldCurrent1=current1
                current1=current1.next
            # save the current, attach the new node and go next of current from the saved current
            newCurrent=current
            oldCurrent1.next=current
            current.next=None
            current=newCurrent.next
        return dummy.next
                
    def partition(self, head, x):
        # separate the list into 2 distinct lists and link them afterwards.
        # p1, p2 traverses the list and hd1 and hd2 are the heads of two lists
        hd1=p1=ListNode(0)
        hd2=p2=ListNode(0)
        while head:
            if head.val<x:
                p1.next=head
                p1=p1.next
            else:
                p2.next=head
                p2=p2.next
            head=head.next
        #join the lists
        p2.next=None
        p1.next=hd2.next
        return hd1.next

    def reverseAlternate(self,head,k):
        #Others
        #reverse every alternate k nodes
        #rirst alternate k nodes and then skip k nodes, do it recursively
        count=0
        prev=None
        curr=head
        count=0
        while curr and count<k:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
            count+=1
        head.next=curr
        count=0
        while count<k-1 and curr:
            curr=curr.next
            count+=1
        if curr:
            curr.next=self.reverseAlternate(curr.next,k)
        return prev
    
    def isPalindrome(self, head):
        # check a list is palindrome
        # reverse first half, and compare with second half
        count = 0
        node = head
        while node:
            node = node.next
            count += 1
        node = head
        pre = None
        for i in range(count // 2):
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        # if odd elements skip the middle
        if count % 2 == 0:
            h2 = node
        else:
            h2 = node.next
        h1 = pre
        while h1:
            if h1.val == h2.val:
                h1 = h1.next
                h2 = h2.next
            else:
                return False
        return True
l=linkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(7)
l.insert(8)
l.insert(9)
#l.insert(4)
#l.insert(5)
#l.insert(5)
#l.insert(1100)

#l1=linkedList()
#l1.insert(0)
#l1.insert(3)
#l1.insert(9)
#l1.insert(15)
#l1.insert(20)

headA=l.getHead()
#headB=l1.getHead()
#l.printList(l.reverseList(headA))
#x=l.reverseBetween(headA,1,2)
#x=l.merge(headA,headB)
#x=l.sortList(headA)
#l.printList(headA)
#l.printList(l.insertionSortList(headA))
#l.printList(l.swapPairs(headA))
#l.printList(l.deleteDuplicates(None))
#l.printList(l.partition(headA,3))
l.printList(l.reverseAlternate(headA,3))
