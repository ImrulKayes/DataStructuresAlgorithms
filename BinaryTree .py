# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root=None
    def insertNode(self,val):
        # insert nodes level-by-level
        newNode=TreeNode(val)
        root=self.root
        if root==None:
            self.root=newNode
            return
        else:
            levelNodes=[]
            levelNodes.append(root)
            while len(levelNodes)!=0:
                nextLevel=[]
                for node in levelNodes:
                    if node.left:
                        nextLevel.append(node.left)
                    else:
                        node.left=newNode
                        return
                    if node.right:
                        nextLevel.append(node.right)
                    else:
                        node.right=newNode
                        return
                levelNodes=list(nextLevel)
                        
    def printTree(self,root):
        # print pre-order traversal of the tree
        if root is None:
            return
        else:
            print root.val
            self.printTree(root.left)
            self.printTree(root.right)

    def returnRoot(self):
        return self.root

    def depth(self,root):
        if not root:
            return 0
        else:
            return max(self.depth(root.left),self.depth(root.right))+1   

    def isBalanced(self, root):
        # in this case, we are reaptedly visiting depth of a node,
        # O(n*n) complexity (because for self.depth(root.left) call a node is called, and for self.isBalanced(root.left) called the node is also called or T(n)=2T(n-2)+O(n)= O(n*n), even more--> time take to solve one sub-problem (n) * total number of subproblems(n)
        # a O(n) solution is below
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.depth(root.left)-self.depth(root.right))<=1

    def isBalanced1(self,root):
        if self.isBalanced(root)==-1:
            return False
        else:
            return True
    def isBalancedUtil(self,root):
        # if current node's subtree are balaced they will retrun max depth (in thise case the node will return max depth), otherwise they will return -1 (in this case the node will return -1)
        if not root:
            return 0
        left=self.isBalancedUtil(root.left)
        if left==-1:
            return -1
        right=self.isBalancedUtil(root.right)
        if right==-1:
            return -1
        if abs(left-right)>1:
            return False
        else:
            return abs(left-right)+1

    def isSymmetric(self, root):
        # Check whether left is a mirror image of right
        # Using iteration, a recursive solution is below
        if root==None:
            return True
        if root.left==None and root.right==None:
            return True
        if root.left==None and root.right:
            return False       
        if root.right==None and root.left:
            return False             

        thisLevel=[]
        thisLevel.append(root.left)
        thisLevel.append(root.right)
        while True:
            nextLevel=[]
            vals=[]
            for node in thisLevel:
                vals.append(str(node.val))
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)

            #print vals
            if len(vals)%2!=0:
                return False
            else:
                mid=int(len(vals)/2)
                if ''.join(vals[0:mid])!=''.join(vals[mid:len(vals)])[::-1]:
                    return False
                else:
                    thisLevel=nextLevel
            if len(thisLevel)==0:
                return True


    def check_symmetry(self, root):
        if root is None: 
            return True 
        else: 
            return self.check_symmetry_recursion(root.left, root.right)

    def check_symmetry_recursion(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False

        return (node1.val == node2.val and 
            self.check_symmetry(node1.left, node2.right) and
            self.check_symmetry(node1.right, node2.left))


    def levelOrderBottom(self, root):
        # Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
        if root is None:
            return []
        else:           
            thisLevel=[]
            output=[]
            thisLevel.append(root)
            output.append([root.val])

            while True:
                nextLevel=[]
                output1=[]
                for node in thisLevel:
                    if node.left is not None:
                        nextLevel.append(node.left)
                    if node.right is not None:
                        nextLevel.append(node.right)
                if len(nextLevel)==0:
                    output.reverse()
                    return output
                else:
                    thisLevel=nextLevel
                    for i in thisLevel:
                        output1.append(i.val)
                    output.append(output1)

    def isSameTree(self, p, q):
        # Return True if two trees are the same, else return False
        if not p and not q:
            return True
        if not p or not q:      # not that you can't write if p or q--> this will return False even when both p and q are equal
            return False
        return  p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            
    def maxDepth(self, root):
      # The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
      if not root:
            return 0
      return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

    def minDepth(self, root):
      # The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
      if not root:
            return 0
      else:
          # if not right node
          if not root.right:
              return self.minDepth(root.left)+1
          # if no left node
          elif not root.left:
              return self.minDepth(root.right)+1
          # else
          else:
              return min(self.minDepth(root.left),self.minDepth(root.right))+1


    def pathSum(self, root, sum1):
        #Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
        if not root:
            return 

        # if this is a leaf node 
        if not root.left and not root.right:
            if root.val==sum1:
                return [[root.val]]

        # if this is not a leaf node
        left=self.pathSum(root.left,sum1-root.val)
        right=self.pathSum(root.right,sum1-root.val)

        # if any left or right calls produce any results
        if left:
            for alist in left:
                alist.insert(0,root.val)
        if right:
            for alist in right:
                alist.insert(0,root.val)
        return left+right 
            
    def preorderTraversal(self, root):
        # pre-order traversal iteritively
        # use FIFO queue
        
        if not root:
            return []
        
        output=[]
        queue=[root]

        while queue:
            # pop queue head
            head=queue.pop(0)
            output.append(head.val)
            # add left after right nodes at the beginning of the queue
            if head.right:
                queue.insert(0,head.right)
            if head.left:
                queue.insert(0,head.left)
        return output  

    def inorderTraversal(self, root):
        # in-order travel iteratively
        if not root:
            return []
        output=[]
        stack=[root]
        current=root
        while stack:
            # push until current has any left child
            if current:
                if current.left:
                    stack.append(current.left)
                current=current.left
            else:
            # if current has no left child, pop, add to output and push right child (if any) of popped item
                top=stack.pop()
                output.append(top.val)
                current=top.right
                if current:
                    stack.append(current)
        return output

    def invertTree(self, root):
        # https://leetcode.com/problems/invert-binary-tree/
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


    def sumNumbers(self, root):
         # Sum Root to Leaf Numbers
         # see the sumPaths in BinaryTree-1
         pass

    def countNodes(self, root):
        # count number of nodes in a binary tree
        if not root:
            return 0
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1          

    def rightSideView(self, root):
        # Compute the right view of both right and left left subtree, then combine them. For very unbalanced trees
        # if rightside goes to upto 2, leftside's from 3 to rest elements will be included
        # OR Traverse the tree level by level and add the last value of each level to the view. This is O(n).
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]

    def zigzagLevelOrder(self, root):
        # this is similar to level order traversal, only difference is we are keeping a flag to track whether left to right should be in the output
        # but levels will be always left to right
        if not root:
            return []        
        current=[root]
        status='L'
        output=[]
        while current:
            next=[]
            output.append([x.val for x in current])
            # if this level is right to left then reverse current (later for will always start from the first node of a level)
            if status=='R':
                current=current[::-1]
            for node in current:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            # if this level->R then next level's output will be from right to left, so copy in that order
            if status=='L':
                current=next[::-1]
                status='R'
            else:
                current=next
                status='L'
        return output

    def flatten(self, root):
        # Given a binary tree, flatten it to a linked list in-place.
        # We simply flatten left and right subtree and paste each sublist to the right child of the root. (don't forget to set left child to null)
        if not root:
            return 
        left,right=root.left,root.right
        self.flatten(left)
        self.flatten(right)

        root.left=None
        root.right = left
        cur = root
        # we have flattened left and right sub-tree, we are going to the firthest right node of left flattened tree (as root.right = left) and setting it's next right node to root's right node
        while cur.right:
            cur = cur.right
        cur.right = right       


    def lowestCommonAncestor(self, root, p, q):
        # if root is equl to either of them then root is the answer (as other one might be left or right subtree)
        # othewise we will recure left and right subtree, if both subtrees return a root then current root is ans, otherwise either one of them (that returns not None) is the ans
        
        if (not root) or (root == p) or (root == q):
            return root

        # search left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # both found, root is the LCA
            return root
        return left or right

    def connect(self,root):
        # opulate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
        # we will start from the root and connect next level elements
        # in the next level root.left is the first node and it's .next is the next node
        # we dont need a queue as start alawys gives the first element of and we can get subsequent using next
        start=root
        while start:
            cur=start
            while cur:
                if cur.left:
                    cur.left.next=cur.right
                # for two node A and B, connect A's right child to B's left child
                if cur.next and cur.right:
                    cur.right.next=cur.next.left
            start=start.left        
        
class Solution:
    # build a tree from inorder and postorder traversals: cosider a sample tree traversals in-order: 4 2 5 (1) 6 7 3 8 post-order: 4 5 2 6 7 8 3 (1)
    # From the post-order array, we know that last element is the root. We can find the root in in-order array.
    #Then we can identify the left and right sub-trees of the root from in-order array. Using the length of left sub-tree, we can identify left and right sub-trees in post-order array. Recursively, we can build up the tree.
    def buildTree1(self, inorder, postorder):
        if not inorder and not postorder:
            return None
        
        if len(inorder)==1:
            newNode=TreeNode(inorder[0])
            newNode.left=None
            newNode.right=None
            return newNode
        
        rootValue=postorder[-1]
        inoderIndexRoot=inorder.index(rootValue)
        newNode=TreeNode(rootValue)
        leftRoot=self.buildTree(inorder[0:inoderIndexRoot],postorder[0:inoderIndexRoot])
        rightRoot=self.buildTree(inorder[inoderIndexRoot+1:len(inorder)],postorder[inoderIndexRoot:(len(postorder)-1)])
        newNode.left=leftRoot
        newNode.right=rightRoot
        return newNode



    def buildTree(self, preorder, inorder):
        # based on the pevios approach
        # infact we dont need to slice pre-order, as when there will be no element in left or right subtree inorder string would be empty
        # this is also true for postorder in previos code
        if not preorder or not inorder:
            return None
        rootValue = preorder[0]
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)
        root.left = self.buildTree(preorder[1:inorderIndex+1], inorder[:inorderIndex])
        root.right = self.buildTree(preorder[inorderIndex+1:], inorder[inorderIndex+1:])
        return root

    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        rootValue = preorder.pop(0)  # then we have to do the pop here
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)

        root.left = self.buildTree(preorder, inorder[:inorderIndex])
        root.right = self.buildTree(preorder, inorder[inorderIndex+1:])

        return root

       
tree=BTree()
tree.insertNode(1)
tree.insertNode(2)
tree.insertNode(3)
tree.insertNode(4)
tree.insertNode(5)
tree.insertNode(6)
tree.insertNode(7)
#tree.insertNode(8)
#tree.insertNode(9)
#tree.insertNode(10)

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
#print tree.depth(root.left)
#print tree.depth(root.right)
#print tree.isBalanced()
#print tree.isSymmetric(root)
#print tree.isSameTree(root,root1)
#print tree.maxDepth(root)
#print tree.minDepth(root)
#print tree.hasPathSum(root,8)
#print tree.pathSum(root,6)
#print tree.inorderTraversal(root)
#root=tree.invertTree(root)
#print tree.sumNumbers(root)
#tree.printTree(root)
#print tree.countNodes(root)
#print tree.rightSideView(root)
#solution=Solution()
#rootA=solution.buildTree([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
#tree.printTree(rootA)
#print tree.zigzagLevelOrder(root)
#tree.flatten(root)
#root=tree.returnRoot()
x=tree.lowestCommonAncestor(root,root.left,root.right)
print x.val


