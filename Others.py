class Stack:    # initialize your data structure here.    def __init__(self):        self.q=[]        def push(self, x):        self.q.append(x)    def pop(self):        self.q.pop()    def top(self):        x=self.q[-1]         return x     def empty(self):        if len(self.q)==0:            return True        else:            return False##s=Stack()##s.push(10)##s.push(20)##s.push(30)##s.top()##s.pop()##s.pop()##print s.empty()class Queue:    # initialize your data structure here.    def __init__(self):        self.q=[]        # @param x, an integer    # @return nothing    def push(self, x):        self.q.append(x)    # @return nothing    def pop(self):        if len(self.q)>0:            self.q=self.q[1:]    # @return an integer    def peek(self):        if len(self.q)>0:            return self.q[0]        else:            return    # @return an boolean    def empty(self):        return len(self.q)==0#s=Queue()#s.push(10)#s.push(20)#s.push(30)#s.pop()#print s.peek()#s.pop()#s.pop()#print s.empty()class circularQueue:    q=[]    def __init__(self,size):        self.q=[0 for i in range(size)]        self.head=-1        self.tail=-1        self.size=size    def enqueue(self,num):        if (self.head==0 and self.tail==self.size-1) or (self.tail+1==self.head):            raise Exception("The queue is full")        else:            self.tail=0 if self.tail==self.size-1 else self.tail+1            self.q[self.tail]=num            if self.head==-1:                self.head=0    def dequeue(self):        if (self.head==-1):  raise Exception("The queue is empty")        else:            temp= self.q[self.head]            if self.head==self.tail:                self.head=-1                self.tail=-1            else:                self.tail=0 if self.head==self.size-1 else self.head+1            return temp    def printQueue(self):        print self.q[self.head:self.tail+1]        #q=circularQueue(3)#q.enqueue(1)#q.enqueue(2)#q.enqueue(3)#q.enqueue(4)#q.printQueue()#q.dequeue()#q.printQueue()class Solution:    # @param {integer} n    # @return {integer}    def trailingZeroes(self, n):        count = 0    # Keep dividing n by powers of 5 and update count    # http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/        i=5        while n/i>=1:            count+=n/i            i=i*5             return count;        def isHappy(self, n):        # for unhappy number, it loops endlessly in a cycle which does not include 1, so if we should keep track of the number and if we have already seen a number and count is still 0 then unhappy        dic={}        count=0        while True:            if dic.has_key(n) and count==0:                return False            dic[n]=1            l=list(str(n))            sum=0            newNumber=[]            for a in l:                sum+=int(a)*int(a)            n=sum            #print n            if sum==1:                if count>1:                    return True                else:                    count+=1    def countPrimes(self, n):        import math        if n<=1:            return 0        output=[]        for i in range(2,n):            count=0            for j in range(2,int(math.sqrt(i))):                if (i%j)==0:                    count+=1                if count>0:                    break            if count==0:                output.append(i)        #print output        return len(output)        def isValid(self, s):        if not s:            return True        stack=[]        for paren in s:            if paren in ['(','[','{']:                stack.append(paren)            else:                if not stack:                    return False                if paren==')':                    top=stack.pop()                    if top!='(':                        return False                if paren=='}':                    top=stack.pop()                    if top!='{':                        return False                                    if paren==']':                    top=stack.pop()                    if top!='[':                        return False        if stack:            return False        else:            return True    def merge(self, nums1, m, nums2, n):        index1=0        index2=0        if m==0:            for i in range(len(nums2)):                nums1[i]=nums2[i]            return         nums1=nums1[0:m]        nums2=nums2[0:n]                while index1<m and index2<n:            if nums2[index2]<=nums1[index1]:                nums1.insert(index1,nums2[index2])                index1+=1                index2+=1            else:                index1+=1        if index1==m and index2<n:            for num in nums2[index2:n]:                nums1.insert(index1,num)                index1+=1        #nums1[0:m+n]=nums1[0:m+n]        #print  nums1    def evalRPN(self, tokens):        if len(tokens)==0:            return         q=[]        q.append(int(tokens[0]))        for i in range(1,len(tokens)):            #print q            if tokens[i] in ('+','-','*','/'):                opt=tokens[i]                b=q.pop()                a=q.pop()                if opt=='+':                    q.append(a+b)                if opt=='-':                    q.append(a-b)                if opt=='*':                    q.append(a*b)                if opt=='/':                    if (a<0 and b>0) or (a>0 and b<0):                        q.append((-1)*int(abs(a)/abs(b)))                    else:                        q.append(int(abs(a)/abs(b)))            else:                q.append(int(tokens[i]))        return q.pop()#Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).#Initially, let p equal 2, the first prime number.#Starting from p, enumerate its multiples by counting to n in increments of p, and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself should not be marked).#Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.            def countPrimes(self, n):        if n>=0 and n<2:            return 0        Mark=[False for i in range(0,n+1)]        #print Mark        p=2        output=[2]        while not Mark[p]:            i=2            while p*i<=n:                #print p*i                Mark[p*i]=True                i+=1            noMarkLeft=True            i=p+1            while i<=n and Mark[i]:                i+=1            if i>n:                break            else:                p=i                output.append(p)        return len(output)    def isPowerOfTwo(self, n):        if n<=0:            return False        if n==1:            return True        while n%2==0:            n=n/2        if n==1:            return True        else:            return False    def multiply(self, num1, num2):        # consider num1=24 and num2=123, result=3*4+20*4+100*4                                            #   3*20+20*20+100*20        result=0        for i,n1 in enumerate(num1[::-1]):            digits1=int(n1)*(10**i)            for j,n2 in enumerate(num2[::-1]):                digits2=int(n2)*(10**j)                result+=digits2*digits1        return result    def countDigitOne(self, n):        count=0        for i in range(n,0,-1):            if '1' in str(i):                count+=1        return count    def simplifyPath(self, path):        folders = []        for c in path.split('/'):            # e.g., /a will make first element None            if not c:                continue            elif c == '.':                continue            elif c == '..':                if len(folders) != 0:                    folders.pop()            else:                folders.append(c)        return '/' + '/'.join(folders)        solution=Solution()#print solution.trailingZeroes(100)#print solution.romanToInt('MMCCCXCIX')#print solution.isHappy(882)#print solution.countPrimes(100)#print solution.isValid("[{}]")#print solution.merge([1,0],1,[2],1)#print(solution.countPrimes(113))#print(solution.containsNearbyAlmostDuplicate([4,5,2,6,7,3],2,6))#print(solution.intToRoman(1))#print(solution.isPowerOfTwo(6))#print solution.multiply("24","123")#solution.countDigitOne(13)