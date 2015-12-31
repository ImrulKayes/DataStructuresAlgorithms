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
        if root is None:
            return
        else:
            print root.val
            self.printTree(root.left)
            self.printTree(root.right)

    def returnRoot(self):
        return self.root

    def bottomTraversal(self,root):
        # Others http://www.geeksforgeeks.org/bottom-view-binary-tree/
        #Bottom View of a Binary Tree Given a Binary Tree, we need to print the bottom view from left to right.
        #A node x is there in output if x is the bottommost node at its horizontal distance. Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1,
        #and that of right child is horizontal distance of x plus 1.
        dic={}
        self.treeAttribites(root,dic,0,0)

        # for each distance we will take first node (as if we have maultiple such nodes only the first/left one is permitted) which has maximum levels
        output=[]
        for k,v in dic.iteritems():
            maxs=-10000
            temp=-10000
            for tuples in v:
                if tuples[1]>maxs:
                    maxs=tuples[1]
                    temp=tuples[0].val
            output.append(temp)
        print output
                    

    def treeAttribites(self,root,dic,level,distance):
        # we will create a dictionary where a each distrance will have list of tuples in the form of (node,level) 
        if not root:
            return
        else:
            dic.setdefault(distance,[]).append((root,level))
            self.treeAttribites(root.left,dic,level+1,distance+1)
            self.treeAttribites(root.right,dic,level+1,distance-1)

    def pairSums(self,root):
        #Given a Balanced Binary Search Tree and a target sum, write a function that returns true if there is a pair with sum equals to target sum, otherwise return false.
        #http://www.geeksforgeeks.org/find-a-pair-with-given-sum-in-bst/
        pass

    def topView(self,root):
        # Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. Given a binary tree, print the top view of it.
        # The output nodes can be printed in any order. Expected time complexity is O(n) A node x is there in output if
        # x is the topmost node at its horizontal distance. Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.

        # use dictionary to infer whether a node is seen in a distace, if distance is new, add the node to the output
        if not root:
            return []
        currentLebel=[(root,0)]
        dic={}
        dic[0]=1
        output=[root.val]
        while currentLebel:
            nextLevel=[]
            for (root,x) in currentLebel:
                # for left child, set it's distance to x-1 and add to output if first in this distance
                if root.left:
                    nextLevel.append((root.left,x-1))
                    if dic.has_key(x-1):
                        pass
                    else:
                        dic[x-1]=1
                        output.append(root.left.val)
                # for right child set it's distance to x-1 and add to output if first in this distance
                if root.right:
                    nextLevel.append((root.right,x+1))
                    if dic.has_key(x+1):
                        pass
                    else:
                        dic[x+1]=1
                        output.append(root.right.val)
            currentLebel=nextLevel
        print output

        
    def diagonalSum(self,root):
        # Diagonal Sum of a Binary Tree http://www.geeksforgeeks.org/diagonal-sum-binary-tree/
        # 1. Add root with vertical distance as 0 to the queue.
        # 2. Process the sum of all right child and right of right child and so on.
        # 3. Add left child current node into the queue for later processing.The vertical distance of left child is vertical distance of current node plus 1. 4.
        # 4. Keep doing 2nd, 3rd and 4th step till the queue is empty.
        if not root:
            return []
        q=[(root,0)]
        dic={}
        while q:
            (node,dis)=q.pop(0)
            # we have already sums for this vertical distance
            sums=dic[dis] if dic.has_key(dis) else 0
            while node:
                sums+=node.val
                if node.left:
                    q.append((node.left,dis+1))
                node=node.right
            dic[dis]=sums
        for k in sorted(dic.keys()):
            print dic[k]         



    def BSTtoBianry(self,root,res):
        # Given a Binary Search Tree (BST), convert it to a Binary Tree such that every key of the original BST is changed to key plus sum of all greater keys in BST.
        # Do reverse inorder traversal, res[0] will store all sums of elements, adjust nodes values
        if not root:
            return None
        self.BSTtoBianry(root.right,res)
        res[0]+=root.val
        root.val=res[0]
        self.BSTtoBianry(root.left,res)


    def sumPaths(self,root):
        # find sum of all the numbers formed by appending the data of nodes from root to leaf node. In a single traversal of the tree.
        # simple, use backtracking
        
        if not root:    return 
        res=[0]
        nums=[]
        self.sumPathsUtil(root,res,nums)
        return res[0]
    
    def sumPathsUtil(self,root,res,nums):
        # if this is a leaf node, add the backtracker chain to result
        if not root.left and not root.right:
            res[0]+=int(''.join(nums+[str(root.val)]))
            return
        # else move to left or right child (if any)
        if root.left:
            self.sumPathsUtil(root.left,res,nums+[str(root.val)])
        if root.right:
            self.sumPathsUtil(root.right,res,nums+[str(root.val)])

    def findHeightFromParentArrayUtil(self,i,parent,depth):
        # If depth[i] is already filled
        if depth[i]:
            return
        # If node at index i is root
        if parent[i]==-1:
            depth[i]=1
            return
        # If depth of parent is not evaluated before, then evaluate
        # depth of parent first
        if depth[parent[i]]==0:
            self.findHeightFromParentArrayUtil(parent[i],parent,depth)
        # Depth of this node is depth of parent plus 1
        depth[i]=depth[parent[i]]+1
            

    def findHeightFromParentArray(self,parent):
        # A given array represents a tree in such a way that the array value gives the parent node of that particular index.
        # The value of the root node index would always be -1. Find the height of the tree. http://www.geeksforgeeks.org/find-height-binary-tree-represented-parent-array/
        # A simple solution is to first construct the tree and then find height of the constructed binary tree. The tree can be constructed recursively by first searching the current root,
        # then recurring for the found indexes and making them left and right subtrees of root. This solution takes O(n2) as we have to linearly search for every node.
        # An efficient solution can solve the above problem in O(n) time. The idea is to first calculate depth of every node and store in an array depth[]. Once we have depths of all nodes, we return maximum of all depths.

        depth=[0 for i in range(len(parent))]
        for i in range(len(parent)):
            self.findHeightFromParentArrayUtil(i,parent,depth)
        return max(depth)

    def shortedPathBetweenTwoNodes(self,node1,node2):
        # get LCA of node1 and node2, dist(LCA,node1)+dist(LCA,node2) or dist(root,node1)+dist(root,node2)-2*() is the ans
        pass
        
tree=BTree()
tree.insertNode(1)
tree.insertNode(2)
tree.insertNode(3)
tree.insertNode(4)
tree.insertNode(5)
#tree.insertNode(6)
root=tree.returnRoot()
#root.left =  TreeNode(2)
#root.right =  TreeNode(3)
#root.left.right =  TreeNode(4)
#root.left.right.right =  TreeNode(5)
#root.left.right.right.right =  TreeNode(6)


#root.left =  TreeNode(2);
#root.right =  TreeNode(3);
#root.left.left =  TreeNode(9);
#root.left.right =  TreeNode(6);
#root.right.left =  TreeNode(4);
#root.right.right =  TreeNode(5);
#root.right.left.left =  TreeNode(12);
#root.right.left.right =  TreeNode(7);
#root.left.right.left =  TreeNode(11);
#root.left.left.right =  TreeNode(10);



#root=tree.returnRoot()
#tree.bottomTraversal(root)
#tree.topView(root)
#tree.diagonalSum(root);

#tree.BSTtoBianry(root,[0])
#tree.printTree(root)
#print tree.sumPaths(root)
print tree.findHeightFromParentArray([-1, 0, 0, 1, 1, 3, 5])

