class Solution(object):
    def hammingWeight(self, n):
        "how many 1's in n?"
        count=0
        x=1
        for i in range(32):
            if n & x:
                count+=1
            x=x<< 1
        return count

    def reverseBits(self, n):
        "reverse n by bits. 1011 will br 1101"
        x=1
        res=0
        for i in range(32):
            "starting last bit, if that is 1 make corresponding bit of res 1" 
            if n & x:
                res=res | 1 << (31-i)
            x=x<<1
        return res
    
    def singleNumber(self, nums):
        # A xor A =0, A xor B xor A =B
        if not nums: return 
        res=nums[0]
        for x in nums[1:]:
            res=res^x
        return res

    def singleNumber(self, nums):
        # Given an array of integers, every element appears three times except for one. Find that single one.
        # Since every number appears 3 times except for one, from the binary perspective, assumed 32 bits integer, then
        # every bit appears 3 times except for some bits. Thus, treat this integer array as a bit matrix, each number is represented in binary form in each row,
        # if we accumulate every bit vertically, and module each sum by 3, the result would be either 0 or 1. And 1 is one bit of the single number.
        res = 0
        for i in xrange(32):
            count = 0
            for num in nums:
                # count whether i'th bit of num is 1
                count += (num >> i) & 1
            rem = count % 3
            # if the number is negative then generate the number (e.g., if 4 bits -2 could be the sum of  (-4) 1000 and (2) 0010) 
            if i == 31 and rem:
                res = (-(1 << 31))+res
            # else make the bit to the appropriate location of res 
            else:                
                res |= rem * (1 << i)
        return res

    def singleNumber(self, nums):
        "in nums exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once."
        "those two numbers at least one bit that are not the same, so xoring all elemens will give where those two numbers are difference beacuse other numbers appears twice and their xor is 0, and dont effect"
        "Find out an arbitrary set bit (for example, the rightmost set bit)."
        "In the second pass, we divide all numbers into two groups, one with the aforementioned bit set, another with the aforementinoed bit unset. Two different numbers we need to find must fall into thte two distrinct groups.
        "XOR numbers in each group, we can find a number in either group."
        
        res=nums[0]
        for num in nums[1:]:
            res=res^num
        "x & (-x) : Returns the rightmost 1 in binary representation of x"
        "Therefore (-x) will have all the bits flipped that are on the left of the rightmost 1 in x. So x & (-x) will return rightmost 1."
        res&=-res
        output=[0,0]
        for num in nums:
            if num&res:
                output[0]^=num
            else:
                output[1]^=num
        return output
        

    def swapNumber(self,a,b):
        # Others
        # swap two numbers without temporary variable
        # note that a^b^a=b
        a=a^b
        b=a^b # b is now a^b^a
        a=a^b # a is now a^b^a, beacuse b already holds a and a hold a^b
        print a,b

    def repeatedCharacter(self,chars):
        # check whether a string has repeated chars
        # assume ascii chars and only lower cases

        # if string has more than 256 chars some chars are repated
        if len(chars)>256: return false

        # checker is used as a bitmap to indicate which characters have been seen already
        # checker is int, so 32 bits, difference between 'z'-'a' is <32, so it can be used as a bitmap
        checker=0
        for char in chars:
            index=ord(char)-ord('a')
            # check whether we have seen the char
            if (checker & (1<<index))>0:
                return False
            else:
            # otherwise mark that the char has been seen
                checker=checker | (1<<index)
        return True

    def romanToInt(self, s):
        # reverse the string, pop two (if exists) and match with dictionary,very naive!
        if len(s)==0:
            return None
        dic={}
        dic['I']=1
        dic['IV']=4
        dic['V']=5
        dic['IX']=9
        dic['X']=10
        dic['XL']=40
        dic['L']=50
        dic['XC']=90
        dic['C']=100
        dic['CD']=400
        dic['D']=500
        dic['CM']=900
        dic['M']=1000

        s=s[::-1]
        s1=list(s)
        num=0
        while s1:
            a=s1.pop()
            if s1:
                b=s1.pop()
                c=a+b
                if dic.has_key(''.join(c)):
                    num+=dic[''.join(c)]
                else:
                    s1.append(b)
                    num+=dic[a]
            else:
                num+=dic[a]
        return num

    def romanToInt(self, s):
        # smart one here. IX=(-1)+10=9, the following utilizes this
        if len(s)==0:
            return
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        p,q=0,1
        sum = 0
        while q<len(s):
            if roman[s[p]]<roman[s[q]]:
                sum+= ((-1)*roman[s[p]])
            else:
                sum += roman[s[p]]
            p,q=q,q+1
        sum+=roman[s[p]]
        return sum


    def intToRoman(self, num):
        if num==0:
            return None
        dic={}
        dic[1]='I'
        dic[4]='IV'
        dic[5]='V'
        dic[9]='IX'
        dic[10]='X'
        dic[40]='XL'
        dic[50]='L'
        dic[90]='XC'
        dic[100]='C'
        dic[400]='CD'
        dic[500]='D'
        dic[900]='CM'
        dic[1000]='M'
        divisors=sorted(dic)[::-1]
        output=[]
        while num>0:
            for divisor in divisors:
                if num/divisor:
                    for j in range(num/divisor):
                        output.append(dic[divisor])
                    num=num%divisor
        return ''.join(output)            

    def decToBibary(self,num):
        output=[]
        while num:
            if num%2:
                output.append('1')
            else:
                output.append('0')
            num=num/2
        return ''.join(output[::-1])
    
    def binaryToDec(self,nums):
        res=0
        for num in nums:
            res=res*2 + int(num)
        return res

    def floatToBinary(self,num):
        # num is between 0 t0 1
        # http://sandbox.mc.edu/~bennet/cs110/flt/dtof.html
        output=['.']
        while num>0:
            r=num*2
            if r>=1:
                output.append('1')
                num=r-1
            else:
                output.append('0')
                num=r
        return ''.join(output)
            
    def stringToLong(self,st):  # or simply this is atoi
        # for 123 we can go either from front e.g., 12=1*10 +2, 123= 12*100 =3 or from back 23= 2*10 +3 , front is good
        if st[0]=='-':
            st1=st[1:]
            flag=1
        else:
            st1=st
            flag=0
        res=0
        mul=0
        # from back
    ##    for i in range(len(st1)-1,-1,-1):
    ##        res=res+(ord(st1[i])-ord('0'))*(10**mul)
    ##        mul+=1
        # from front 
        for i in range(len(st1)):
            res=res*10+(ord(st1[i])-ord('0'))
        if flag:
            return -1*res
        else:
            return res
        
    def myAtoi(self, str):
        """
        convert a string to int
        """
        st=str
        if not st: return 0

        "get rid of front whitespaces"
        i=0
        while st[i]==" ":
            i+=1
        st=st[i:]
        if not st: return 0
    
        "what is the sign?"
        if st[0]=='+':
            st1=st[1:]
            flag=0
        elif st[0]=='-':
            st1=st[1:]
            flag=1
        else:
            st1=st
            flag=0

        "convert until end of the string or any invalid chars"
        res=0
        mul=0
        for i in range(len(st1)):
            if not (st1[i]>='0' and st1[i]<='9'):
                break
            res=res*10+(ord(st1[i])-ord('0'))

        "we can only return 2**31 -1 to -2**31" 
        if flag:
            res=-1*res
            return -2**31 if res< -2**31 else res 
        return (2**31) -1 if res>(2**31) -1 else res

    def convertToTitle(self, n):
        # given 1= A and Z=26, convert an integer to nums,e.g., 28=AC=1*26+3, 53=BA=2*26+1
        ans = ''
        while n:
            ans = chr(ord('A') + (n - 1) % 26) + ans
            n = (n - 1) / 26
        return ans

    def titleToNumber(self, s):
        length = len(s)
        total = 0
        for i in range(length):
            total=total*26+(ord(s[i])-ord('A')+1)
        return total
        
    def GCDUtil(self,a,b):
        while a:
            t=b%a
            b=a
            a=t
        return b

    def GCD(self,nums):
        # return gcd of an array of integrs
        nums=sorted(nums)
        ans=nums[0]
        for num in nums[1:]:
            ans=self.GCDUtil(ans,num)
        return ans

    def isUgly(self, num):
        """
        Write a program to check whether a given number is an ugly number.
        Ugly numbers are positive numbers whose prime factors only include 2,3,5
        Below lessons from that a number can be presented with only prime factors
        """
        if num>0:
            for p in [2,3,5]:
                while num%p==0:
                    num=num/p
        return num==1

    def prime(nums):
        # efficiently generate nums number of prime number
        # we will incrementally generate prime numbers, for a number if it is divisible by any of previously generated prime numbers then this is not prime.
        # note that any number can be expressed by prime factors
        
        output=[2]
        for i in range(1,nums):
            nextNumber=output[-1]+1
            while True:
                found=True
                for num in output:
                    if nextNumber%num==0:
                        found=False
                        break
                if found:
                    output.append(nextNumber)
                    break
                nextNumber+=1
        print output
        
    def isPowerOfThree(self, n):
        if n==0: return False
        if n==1: return True
        x=1
        while x<n:
            x=x*3
        return x==n

    def evaluateExpression(self,token):
        "100*(2+12)/14==100"
        "consider +,-,*,/ operands and (,)"
        value=[]
        ops=[]
        i=0

        "cannot use for because we will change i e.g., 300"
        while i<len(token):
            "if space skip this"
            if token[i]==' ':
                i+=1
            elif token[i]>='0' and token[i]<='9':
                "if number the append to value"
                st=[]
                while i<len(token) and token[i]>='0' and token[i]<='9':
                    st.append(token[i])
                    i+=1
                value.append(int(''.join(st)))               
            elif token[i]=='(':
                "if ( append to ops"
                ops.append(token[i])
                i+=1
                
            elif token[i]==')':
                "if ) evaluate the expression until we find beginning (, precession doesnt matter e.g., 2*3+5"
                while ops[-1]!='(':
                    value.append(self.eval(ops.pop(),value.pop(),value.pop()))
                ops.pop()
                i+=1
                
            elif token[i] in '+-*/':
                'if operator evalutes all operator has greater presedence than this operator'
                while ops and self.hasPrecedence(token[i],ops[-1]):
                    value.append(self.eval(ops.pop(),value.pop(),value.pop()))
                ops.append(token[i])
                i+=1            

        'Entire expression has been parsed at this point, all operator have same presendence, apply remaining, ops to remaining values'
        while ops:
            value.append(self.eval(ops.pop(),value.pop(),value.pop()))
        return value.pop()

    def hasPrecedence(self,op1,op2):
        'as we appended parentheses also in the ops queue 1+(2* will give us situation in presedence checking'
        if op2=='(':
            return False
        if op1 in '*/' and op2 in '+-':
            return False
        else:
            return True
        
    def eval(self,op,b,a):
        if op=='+': return a+b
        if op=='-': return a-b
        if op=='*': return a*b                                             
        if op=='/':
            if b==0:
                raise ValueError('Cannot divide by zeor')
            return a/b
        return 0

    def evalRPN(self, tokens):
        "Evaluate reverse polish notation https://leetcode.com/problems/evaluate-reverse-polish-notation/"
        "21+3*-->(2+1)*3"
        
        if len(tokens)==0:
            return 
        q=[]
        q.append(int(tokens[0]))
        for i in range(1,len(tokens)):
            if tokens[i] in ('+','-','*','/'):
                opt=tokens[i]
                b=q.pop()
                a=q.pop()
                if opt=='+':
                    q.append(a+b)
                if opt=='-':
                    q.append(a-b)
                if opt=='*':
                    q.append(a*b)
                if opt=='/':
                    if (a<0 and b>0) or (a>0 and b<0):
                        q.append((-1)*int(abs(a)/abs(b)))
                    else:
                        q.append(int(abs(a)/abs(b)))
            else:
                q.append(int(tokens[i]))
        return q.pop()

    
solution=Solution()
#print solution.singleNumber([1,1,1,2,2,-3])
#print solution.repeatedCharacter("abca")
#print solution.floatToBinary(.625)
#print solution.decToBibary(7)
#print solution.GCD([9,21,12,15,27])
print solution.binaryToDec('1010')
