class TrieNode:
    # Initialize your data structure here.
    def __init__(self, val=None):
        self.val = val
        self.children = {}  # char -> node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        n = len(word)
        curr = self.root
        for i in range(n):
            char = word[i]
            if not char in curr.children:
                for j in range(i, n):
                    curr.children[word[j]] = TrieNode()
                    curr = curr.children[word[j]]
                break
            else:
                curr = curr.children[char]
        curr.val = word


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        n = len(word)
        curr = self.root
        for i in range(n):
            char = word[i]
            if not char in curr.children:
                return False
            curr = curr.children[char]
        return curr.val == word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        n = len(prefix)
        curr = self.root
        for i in range(n):
            char = prefix[i]
            if not char in curr.children:
                return False
            curr = curr.children[char]
        return True

##trie = Trie()
##
##trie.insert("a")
##
###trie.printTree(trie.getRoot())
##trie.insert("ab")
##
##trie.printTree(trie.getRoot())

#trie.insert("ab")

#trie.insert("adc")

#trie.insert("bdc")

#print trie.search("abc")
#print trie.search("ab")
#trie.insert("ab")

#print trie.search("a")
                 
#print trie.startsWith("ias")
#trie.printTree(trie.getRoot())
# trie.search("key")



class WordDictionary:

    # initialize your data structure here.

    def __init__(self):
        self.root = TrieNode()

    # addition is similar to Trie
    # e.g., for "abc" create three nodes a->b->c and c node will hold value abc
    # for abcd, create one additional node d (it will hold abcd) and link it as a children of c
    # a Trie node consits of children dictionary (to capture values on edges and corresponding child) and val
    def addWord(self, word):

        n = len(word)
        curr = self.root
        for i in range(n):
            char = word[i]
            if not char in curr.children:
                for j in range(i, n):
                    curr.children[word[j]] = TrieNode()
                    curr = curr.children[word[j]]
                break
            else:
                curr = curr.children[char]
        curr.val = word        



    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.

    def search(self, word):
        # Took me 2 hours to pass all the test cases!
        return self.search1([self.root],word,'')      

    def search1(self,roots,toMatch,word):
        # toMatch= what left to match, word=exactly what to match, note that if input is a.d and a leaf node value is asd then we shall return True,
        # in this case we will go the leaf node with asd value not a.d 

        # if no input remaining. if any of the root has value equal what to match then return true, else false 
        if not toMatch:
            for root in roots:
                if root.val==word:
                    return True
            return False

        # if current char is . then starting searching for all the childs to match next chars, note that we are mutating original word in this case to support .
        if toMatch[0]=='.':
            for root in roots:
                for k,v in root.children.iteritems():
                    if self.search1([v],toMatch[1:],word+k):
                        return True
            return False

        # else  start searching for all the childs to match next chars.
        else:
            for root in roots:
                for k,v in root.children.iteritems():
                    if toMatch[0]==k:                       
                        if self.search1([v],toMatch[1:],word+k):
                            return True                           
            return False

wordDictionary=WordDictionary()
##wordDictionary.addWord("at")
##wordDictionary.addWord("and")
##wordDictionary.addWord("an")
##wordDictionary.addWord("add")
##print wordDictionary.search("a")
##print wordDictionary.search(".at")
##wordDictionary.addWord("bat")
##print wordDictionary.search(".at")
##print wordDictionary.search("and")
##print wordDictionary.search(".a")
##print wordDictionary.search("a.")
##
##wordDictionary.addWord("at")
##wordDictionary.addWord("and")
##wordDictionary.addWord("an")
##wordDictionary.addWord("add")
##print wordDictionary.search("a")
##print wordDictionary.search(".at")
##wordDictionary.addWord("bat")
##print wordDictionary.search(".at")
##print wordDictionary.search("an.")
##print wordDictionary.search("a.d.")
##print wordDictionary.search("b.")
##print wordDictionary.search("a.d")
##print wordDictionary.search(".")

#print wordDictionary.search("ad")


##wordDictionary.addWord("ran")
##wordDictionary.addWord("rune")
##print wordDictionary.search("r.n"

