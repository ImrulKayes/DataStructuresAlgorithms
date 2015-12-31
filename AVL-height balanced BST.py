# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution1:
    # Height balanced tree is also called AVL tree
    # http://webdocs.cs.ualberta.ca/~holte/T26/avl-trees.html shows how to create an AVL tree from any input
    # Here we have used the heuristics from the sorted array to build the tree
    # the idea is to firt build BST from in incoming put, then check at the root whether left and right subtree has height differences more than 1
    # if more than 1 then make the right child of root as root and make root the leftchild of new root
    # however this is expensive, but it gives an insignt on how to build an AVL tree
    # a better solution is below
    def insertNode(self,val,root):
        newNode=TreeNode(val)
        current=root
        while True:
            if val<=current.val:
                if current.left is None:
                    newNode=TreeNode(val)
                    current.left=newNode
                    return 
                else:
                    current=current.left
            else:
                if current.right is None:
                    newNode=TreeNode(val)
                    current.right=newNode
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


    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None

        root=TreeNode(nums.pop(-0))
        for i in range(len(nums)):
            self.insertNode(nums[i],root)

            if (self.heightBST(root.right)-self.heightBST(root.left))>1:
                leftNode=root
                newRoot=root.right
                newRootOldLeft=newRoot.left
                newRoot.left=leftNode
                
                leftNode.right=newRootOldLeft
                root=newRoot
                
        self.printTree(root)
        
    def heightBST(self,root):
        if root==None:
            return 0
        else:
            return 1+ max(self.heightBST(root.left),self.heightBST(root.right))

class Solution:
    def sortedArrayToBST(self, num):
        # make the root at middle, build tree from left and right inputs
        if not num:
            return None

        mid = len(num) // 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root

    def sortedListToBST(self, head):
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        return self.sortedArrayToBST(nums)
        
solution=Solution()
solution.sortedArrayToBST([0,1,2,3,4,5,6,7])
print tree.heightBST(root.right)


