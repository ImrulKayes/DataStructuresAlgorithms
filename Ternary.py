"Ternary search Tree: https://www.youtube.com/watch?v=CIGyewO7868"
class Node:
    
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.eq=None
        self.left=None
        self.isEndOfString=0

class Ternary:
    
    def insert(self,root,word):
        if not root:
            "add a new node with char if root none (means char not present)"
            root=Node(word[0])
        "create left or right nodes if char is less or greater"
        if word[0]<root.data:
            root.left=self.insert(None,word)
        elif word[0]>root.data:
            root.right=self.insert(None,word)
        else:
        "else the created node's case and proceeds with new elements"
            word=word[1:]
            if word:
                root.eq=self.insert(None,word)
            else:
                root.isEndOfString=1
        return root

    def search(self,root,word):
        if not root:
            return False
        if word[0]<root.data:
            return self.search(root.left,word)
        elif word[0]>root.data:
            return self.insert(root.right,word)
        else:
            word=word[1:]
            if word:
                return self.search(root.eq,word)
            else:
                if root.isEndOfString:
                    return True
                else:
                    return False

root=None
ternary=Ternary()
root=ternary.insert(root,"cat")
root=ternary.insert(root,"bat")
root=ternary.insert(root,"cats")
print ternary.search(root,"bat")
