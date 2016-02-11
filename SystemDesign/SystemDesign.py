'''Design an Url shortener (say 6 chars long)Solution: we will store urls in db with long int id, 2**64 url possilbleNow we have to convert this id to a 6 char url. We have a-z, A-Z, 0-9 = total 62 charsWe can convert the id to a 62base number based on the following encodeURL function. And using decodeURL, we can convert the URL to id and hence to the original db stored URLWhy this would work? Consider a 6 char URL, it can represent 62*62**4+62*62**3+ 62*62**2+ 62*62**1+62  total id's.More: http://www.geeksforgeeks.org/how-to-design-a-tiny-url-or-url-shortener/, http://stackoverflow.com/questions/742013/how-to-code-a-url-shortener'''def encodeURL(n):    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"        output=[]    while n>0:        output.insert(0,chars[n%62])        n=n/62    return ''.join(output)def decodeURL(shortURL):    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"        num=0    for char in shortURL:        num=num*62+chars.index(char)    return numprint encodeURL(12345)print decodeURL("dnh")'''Implement LRU cacheSolution: use a dictionary and doubly linked list.dictionary indicates whether a given page (e.g., int) is in the LRU i.e., linked list.If a page is serviced it is brought in the front (easily implemented by deleting the page and add a new on front), if page needs to detele (e.g., capasity reached) the rear node is deletedin the folowing opposite way is implemented'''class Node:    def __init__(self, k, v):        # let's k is node's page number, v is the value of the node        self.key = k        self.val = v        self.prev = None        self.next = Noneclass LRUCache:    def __init__(self, capacity):        self.capacity = capacity        self.dic = dict()        # in doubly lined list, we first create two dummy node as head and tail        # head's next points to tail and tail's prev points to head. head's prev and tail's next are pointed to None (from __init__)        # new nodes will be inserted between head and tail        self.head = Node(0, 0)        self.tail = Node(0, 0)        self.head.next = self.tail        self.tail.prev = self.head    def get(self, key):        # if the key is in dic, remove the node and add a new node at back        if key in self.dic:            n = self.dic[key]            self._remove(n)            self._add(n)            return n.val        return -1    def set(self, key, value):        # if node is there delete it        if key in self.dic:            self._remove(self.dic[key])        # add a same node to the end        n = Node(key, value)        self._add(n)        self.dic[key] = n        # if capacity exceeds rmove from the front        if len(self.dic) > self.capacity:            n = self.head.next            self._remove(n)            del self.dic[n.key]    def _remove(self, node):        p = node.prev        n = node.next        p.next = n        n.prev = p    def _add(self, node):        p = self.tail.prev        p.next = node        self.tail.prev = node        node.prev = p        node.next = self.tail    