class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BSTtoDLink(root):
    if not root:
        return None
    
    headLeft=BSTtoDLink(root.left)
    headRight=BSTtoDLink(root.right)

    if headLeft:
        head=headLeft
        while headLeft.right:
            headLeft=headLeft.right
        headLeft.right=root
        root.left=headLeft
        root.right=headRight
        if headRight:
            headRight.left=root
        return head
    else:
        if headRight:
            root.right=headRight
            root.left=None
            headRight.left=root
            return root
        else:
            return root


a=TreeNode(10)
b=TreeNode(12)
c=TreeNode(15)
d=TreeNode(25)
e=TreeNode(30)
f=TreeNode(36)
a.left=b
a.right=c
c.left=f
b.left=d
b.right=e
root=BSTtoDLink(a)
while root:
    print root.val
    root=root.right
