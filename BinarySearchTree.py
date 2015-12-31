# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    # @param root, a binary search tree's root node

    def __init__(self, root):
        self.lists=self.printSortedTree(root)
        self.nextToGo=0

    def hasNext(self):
        if self.nextToGo>len(self.lists)-1:
            return False
        else:
            return True
    def next(self):
        toGo=self.lists[self.nextToGo]
        self.nextToGo+=1
        return toGo

    def printSortedTree(self,root):
        # very intuitive, binary tree inorder traversal
        if root is None:
            return []
        else:
            lists=self.printSortedTree(root.left)
            lists.append(root.val)
            lists2=self.printSortedTree(root.right)
            return lists+lists2

class BTree1:
    def __init__(self):
        self.root=None
    def insertNode(self,val):
        newNode=TreeNode(val)
        root=self.root
        if root==None:
            self.root=newNode
            return
        else:
            current=root
            while True:
                if val<=current.val:
                    if not current.left:
                        current.left=TreeNode(val)
                        return 
                    else:
                        current=current.left
                else:
                    if not current.right:
                        current.right=TreeNode(val)
                        return 
                    else:
                        current=current.right
                        
    def printTree(self,root):
        if root is None:
            return
        else:
            print root.val
            self.printTree(root.left)
            self.printTree(root.right)

    def printSortedTree(self,root):
        if root is None:
            return []
        else:
            lists=self.printSortedTree(root.left)
            lists.append(root.val)
            lists2=self.printSortedTree(root.right)
            return lists+lists2

    def returnRoot(self):
        return self.root

    def isValidBST1(self, root):
        # another solution below using stack
        stack = []
        nodes = []        
        while True:
          while root:
            stack.append(root)
            root = root.left
          if not stack:
            return True
          right_root = stack.pop()
          if nodes and right_root.val <= nodes.pop():
            return False
          nodes.append(right_root.val)
          root = right_root.right
          
    def printSortedTree(self,root):
        # very intuitive, binary tree inorder traversal
        # The iterative version of the algorithm using stack is below
        #1) Create an empty stack S.
        #2) Initialize current node as root
        #3) Push the current node to S and set current = current->left until current is NULL
        #4) If current is NULL and stack is not empty then 
        #a) Pop the top item from stack.
        #b) Print the popped item, set current = popped_item->right 
        #c) Go to step 3.
        #5) If current is NULL and stack is empty then we are done.
        if root is None:
            return []
        else:
            lists=self.printSortedTree(root.left)
            lists.append(root.val)
            lists2=self.printSortedTree(root.right)
            return lists+lists2
            
    def isValidBST(self, root):
        # cheating a bit. We know that in-order traversal of a BST gives sorted order. If we don't get that then no BST
        # or an elegeant solution is below
        if root==None:
            return True
        lists=self.printSortedTree(root)
        print lists
        for i in range(1,len(lists)):
            if int(lists[i-1])>=int(lists[i]):
                return False
        return True
    
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
     #Pass down two parameters: lessThan (which means that all nodes in the the current subtree must be smaller than this value) and largerThan (all must be larger than it).
     #Compare root of the current subtree with these two values. Then, recursively check the left and right subtree of the current one. Take care of the values passed down.
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))

    
    def kthSmallest1(self, root, k):
        # inorder traversals gives the sorted order. So, kth smallest is the k-1 th element in the inorder list
        # another solution is below
        if root==None:
            return None
        x=self.printSortedTree(root)
        return x[k-1]

    def kthSmallest(self, root, k):
        number=[0] # for result
        count=[k] # count 
        self.kthSmallestHelper(root,count,number)
        return number[0]
    def kthSmallestHelper(self,root,count,number):
        if root.left:
            self.kthSmallestHelper(root.left,count,number)
        if count[0]==0:
            number[0]=root.val
            return
        if root.right:
            self.kthSmallestHelper(root.right,count,number)

    def numTrees1(self, n):
        # brute force. get all permutations of numbers (all possible traversals), exceeds time limit.
        if n==0:
            return 0        
        if n==1:
            return 1
        if n==2:
            return 2
        output=[]
        for i in range(1,n+1):
            output.append(i)
        lists=self.permute(output)
        dic={}
        #print lists
        for x in lists:
            if (int(x[0])>int(x[1]) and int(x[0])<int(x[2])) :
                dic[''.join(x[0]+x[1]+x[2])]=x
            elif int(x[0])<int(x[1]) and int(x[0])>int(x[2]):
                dic[''.join(x[0]+x[2]+x[1])]=x
            else:
                dic[x]=x
        return len(dic)


    def numTrees(self, n):
        # DP, e.g., if for [1,2,3,4,5], if we consider 3 a root then #BST([1,2])*BST([4,5]) are total BSTs having 3 as root. we can do this for all numbers and sum
        # G(n): the number of unique BST for a sequence of length n.
        # F(i, n), 1 <= i <= n: the number of unique BST, where the number i is the root of BST, and the sequence ranges from 1 to n.
        # G(n) = F(1, n) + F(2, n) + ... + F(n, n). G(0)=1, G(1)=1.
        # F(i, n) = G(i-1) * G(n-i)   1 <= i <= n
        
        G=[0 for i in range(n+1)]
        G[0],G[1]=1,1
        for i in range(2,n+1):
            # all possible combination of left and right and sum
            for j in range(1,i+1):
                G[i]+=G[j-1]*G[i-j]
        return G[n]

    def generateTrees(self, n):
        # it uses the same concept from numTrees
        # if for [1,2,3,4,5], if we consider 3 a root then, roots from(BST([1,2]))*root and from (BST([4,5]))*root are possible left and right children of current root. we can do this for all numbers and retrun the root
        # note that we can use DP, as the recursion is doing some stuffs again and again (e.g, BST([4,5]) needs to do when considering 1,2,3 as roots), but that would be some pain :(

        if n==0:
            return [[]]
        return self.BST([i+1 for i in range(n)])

    def BST(self, nums):
        if not nums:
            return [None]
        output=[]
        for i in range(len(nums)):
            rootListLeft=self.BST(nums[:i])
            rootListRight=self.BST(nums[i+1:])
            for x in rootListLeft:
                for y in rootListRight:
                    newRoot=TreeNode(nums[i])
                    newRoot.left=x
                    newRoot.right=y
                    output.append(newRoot)
        return output

    def lowestCommonAncestor1(self, root, p, q):
        # we are getting the paths that end at p and q
        # then the last last common node from the beginning of two lists is the LCA
        # a much much simpler version is below
        path1=self.pathToNode(root,p)
        path2=self.pathToNode(root,q)

        output=path1[0]
        while path1 and path2:
            x,y=path1.pop(0),path2.pop(0)
            if x.val!=y.val:
                return output
            else:
                output=x
        #if either of the list ends
        return  output
        
    def pathToNode(self,root,p):
        if not root:
            return []
        if root.val==p.val:
            return [root]
        lists1=self.pathToNode(root.left,p)
        lists2=self.pathToNode(root.right,p)
        if lists1 or lists2:
            return [root]+lists1+lists2
        else:
            return []

    def lowestCommonAncestor(self, root, p, q):
        # if both elements are greather than the root, then solution is in right tree
        # if both elements are smaller than the root, then solution is in left tree
        # else the root is the solution, because on element is less(/euql) and other greater(/euql) 
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
    def successorInorder(self,root,node):
        # In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree. Inorder Successor is NULL for the last node in Inoorder traversal.
        # http://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/
        # if node has right subtree then min of right subtree is the successor
        if node.right:
            curr=node.right
            while curr.left:
                curr=curr.left
            return curr
        # otherwise, travel using root pointer until we see a node which is left child of it's root. the root of such a node is the successor
        else:
            while root:
                if node.val<root.val:
                    succ=root
                    root=root.left
                elif node.val>root.val:
                    root=root.right
                else:
                    break
            return succ


tree=BTree1()
tree.insertNode(5)
tree.insertNode(3)
tree.insertNode(2)
tree.insertNode(4)
tree.insertNode(9)
tree.insertNode(8)
tree.insertNode(10)

##tree1=BTree()
##tree1.insertNode(1)
##tree1.insertNode(2)
##tree1.insertNode(3)
##tree1.insertNode(4)
##tree1.insertNode(3)
##tree1.insertNode(4)
##tree1.insertNode(3)

root=tree.returnRoot()
#root1=tree1.returnRoot()

#tree.printTree(root)
#print "---"
#print tree.printSortedTree(root)
#i,v = BSTIterator(None),[]
#while i.hasNext():
#    v.append(i.next())
#print v

#tree.numTrees(4)
#tree1=BTree1()
#print tree1.isValidBST(root)
print tree.kthSmallest(root,3)
#print tree.numTrees(3)

#x=tree.lowestCommonAncestor(root,root.left,root.left.right)
#print x.val

