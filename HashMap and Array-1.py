class Solution:
    # The gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
    # for 1 bits grey code is 0,1. 2 bits, grey code is 00, 01,11,10.
    # cosider 2 bits. intitally output 00, then we filp fist bit, 00,01, taking this in reverse and flipping second bit and adding to original gives 00,01,11,10
    # this code is okay but big and time consuming, an elegent solution is below
    def grayCode(self, n):
        if n==0:
            return [0]
        
        nums=['0' for i in range(n)]
        output=[nums]
       
        for i in range(len(nums)-1,-1,-1):
            temp=list(output)
            for j in range(len(output)-1,-1,-1):
                if output[j][i]=='1':
                    x=output[j][0:i]+['0']+output[j][i+1:]
                else:
                    x=output[j][0:i]+['1']+output[j][i+1:]
                output.append(x)
        output1=[]
        for x in output:
            output1.append(int(''.join(x),2))
        return output1

    def grayCode1(self, n):
        # also doing the same thing as previous, but rather than flipping it is adding 1 as a leftmost bit
        ret = [0]
        for k in range(0, n):
            # e.g, if perviosly ret=0,1,3,2 now afthe the for loop ret will be 0,1,3,2,2+4,3+4,1+4,0+4 which is a grey code of n=3
            for i in range(len(ret)-1, -1, -1):
                ret.append(ret[i]+(2**k)) 
        return ret                

    def nextPermutation(self, nums):
        # based on http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html
        # also see https://en.wikipedia.org/wiki/Permutation
    
        i = l = len(nums)-1
        while i > 0:
            # find the right most pair where nums[i] > nums[i-1]
            if nums[i] > nums[i-1]:
                tmp = 0
                for j in xrange(l, i-1, -1):
                    if nums[j] > nums[i-1]:
                        tmp = j
                        break
                # exchange nums[i-1] and the right most element which larger than nums[i-1] 
                nums[i-1], nums[tmp] = nums[tmp], nums[i-1]
                # reverse from i to the end
                for j in xrange(i, 1+i+(l-i)/2):
                    nums[j], nums[l+i-j] = nums[l+i-j], nums[j]
                break
            i -= 1
        # if nums are in descending order
        if i == 0:
            nums.reverse()
        return nums
    
    def nextPermutation(self,ii):
        #iis=map(int,str(ii))
        iis=[int(x) for x in str(ii)]
        for i in reversed(range(len(iis))):
            if i == 0: return ii
            if iis[i] > iis[i-1] :
                break        
        left,right=iis[:i],iis[i:]
        for k in reversed(range(len(right))):
            if right[k]>left[-1]:
               right[k],left[-1]=left[-1],right[k]
               break
        return int("".join(map(str,(left+sorted(right)))))
    
    def getPermutation(self, n, k):
        import math
        if k not in range(1,math.factorial(n)+1):
            return
        nums=[str(i) for i in range(1,n+1)]       
        for i in range(1,k):
            nums=self.nextPermutation(nums)
        return ''.join(nums)

    def getPermutation(self, n, k):
        # based on http://yucoding.blogspot.com/2013/04/leetcode-question-68-permutation.html
        nums, result = [i + 1 for i in range(n)], ''

        while n > 0:
            totalCount = math.factorial(n - 1)
            index = (k - 1) / totalCount
            result += str(nums.pop(index))
            n -= 1
            k %= totalCount

        return result

    def lengthOfLongestSubstring(self, s):
        # Given a string, find the length of the longest substring without repeating characters.
        # For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
        
        # maxs is the answer
        # dic contains running sub-string, it a repeat is found update maxs and delete all chars from the beginning to the fist occurance of the double
        # p holds the end of the current running sub-string, in case of deletion it needs to be updated
        # if no double found len(dic) is the answer
        if len(s)==0:
            return 0
        maxs=-1000
        dic={}
        p=0
        for i in range(len(s)):
            if dic.has_key(s[i]):
                maxs=len(dic) if len(dic)>maxs else maxs
                for j in range(p,i):
                    if s[j]!=s[i]:
                        del dic[s[j]]
                    else:
                        p=j+1
                        break
                dic[s[i]]=1
            else:
                dic[s[i]]=1
        return max(maxs,len(dic))

    def longestPalindrome1(self, s):
        # obviously this naive apporach will get runtime exceed!
        if len(s)<=1:
            return s
        strs=''
        lens=-1000
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    if len(s[i:j+1])>lens:
                        lens=len(s[i:j+1])
                        strs=s[i:j+1]
        return strs
    
    def productExceptSelf(self, nums):
        # Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
        # Solve it without division and in O(n).
        # Two pass in first pass res holds product of all elements on left of nums[i] excluding nums[i]
        # in second pass, starting from the second of tail, temp holds  product of all elements on on right of nums[i], we multiply temp *res[i]  
        res=[1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]

        temp = 1
        for i in range(len(nums)-2,-1,-1):
            temp=temp*nums[i+1]
            res[i]*=temp
    
        return res

    def longestPalindrome(self, s):
        # Given a string S, find the longest palindromic substring in S.
        # The key intuition of this algorithm is that palindromes are made up of smaller palindromes. So, a palindrome of length 100 (for example), will have a palindrome of
        # length 98 inside it, and one of length 96, ... 50, ... 4, and 2. Because of this, we can move across our string, checking if the current place is a palindrome of a particular length (the longest length palindrome
        # found so far + 1), and if it is, update the longest length, and move forward. 

        # two cases when encountering an new char x: x-maxlen is a palindrome or x-maxlen-1 is a palindrome
        # with length x, then x+2, x+4, ...

        # Example:
        # "xxABCDCBAio"
        #  0123456789  < indexes
        # As we scan our string, we initially find a palindrome of length 2 (xx)
        # We always look backwards!
        # When we get to index 2,3,4, we see no length 3+ palindrome ending there.
        # But when we get to index 6, looking back 3 characters, we see "CDC"! So our
        # longest palindrome is now length 3.
        # At index 7, we look back and see no length 4 palindromes, but find one of
        # length 5 ("BCDCB").
        # And finally, by i = 8, we find the full "ABCDCBA"
        
        longest_index = 0
        max_length = 0
        for i in xrange(len(s)):
            # e.g., aaa, i pointing second a and max_length is already 2
            if self.is_palindrome(s, i - max_length, i):
                longest_index = i - max_length
                max_length = max_length + 1
            # e.g., ABCDCBA last A and max_length is 5 ("BCDCB")
            elif i - max_length - 1 >= 0 and self.is_palindrome(s, i - max_length - 1, i):
                longest_index = i - max_length - 1
                max_length = max_length + 2

        return s[longest_index:longest_index + max_length]

    def is_palindrome(self,string, start, end):
        for i in xrange((end - start + 1) / 2):
            if string[start + i] != string[end - i]:
                return False
        return True

    def findRepeatedDnaSequences(self, s):
        # for each char we look a 10 chars string and increses it's count
        # finally count>1 chars are the answers. why is this a medium problem???
        dic={}
        for i in range(len(s)-9):
            if dic.has_key(s[i:i+10]):
                dic[s[i:i+10]]+=1
            else:
                dic[s[i:i+10]]=1
        output=[]
        #print dic
        for k,v in dic.iteritems():
            if v>1:
                output.append(k)
        return output

    def missingNumber(self, nums):
        # Given an array containing n distinct numbers taken from 0 to n,  find the one that is missing from the array.
        # difference between sum of n numbers that should be n(n+1)/2, and that we are getting from sum(nums) is the answer
        n=len(nums)
        return ((n+1)*n/2)-sum(nums)

    def containsNearbyAlmostDuplicate1(self, nums, k, t):
        # for each possible (i,j) pair in nums, we store the differences of nums(i)-nums(j) in dictionary. Later we check whether conditions on k and t are met
        # it has O(n*n) time and thus time limit exceeded
        
        if len(nums)<2:
            return False
        
        dic={}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    dic.setdefault(i-j,[]).append(nums[i]-nums[j])
        #print dic

        for key,v in  dic.iteritems():
            if k<=key:
                for vals in v:
                    if vals<=t:
                        return True
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is
        # at most t and the difference between i and j is at most k.
        # ind is an array of the indexes of sorted num. Iterate through ind to check if nums are within t and ind are within k.
        # the difference with the bruce force is that here we have less comparisons, first iteration compares len(nums)-1 times, second len(nums)-1 and final one only one time
        ind = sorted(range(len(nums)), key = lambda x: nums[x])
        for i in range(len(nums)-1):
            j = i + 1
            while j < len(nums) and nums[ind[j]] - nums[ind[i]] <= t:
                if abs(ind[i]-ind[j]) <= k:
                    return True
                j += 1
        return False
    
    def CommonElements(arrays):
        # Others:  given a nxn arrays (each row is sorted), find all common elements
        # we will check consequtive arrays, other than common elements all will be marks as -Inf, non -Inf elements in the final array is the answer
        M=len(arrays)
        for m in range(1,M):
            i,j=0,0
            while i<M and j<M:
                #if this element of previous row is greater, mark this element as -Inf and move to next element
                if arrays[m-1][i]>arrays[m][j]:
                    arrays[m][j]=float('-Inf')
                    j+=1
                #if this element of previous row is smaller, mark move to next element of the previous row                   
                elif arrays[m-1][i]<arrays[m][j]:
                    i+=1
                #else move to both rows' next element
                else:
                    i+=1
                    j+=1
            #if this still we have some elements in this row then mark all of them as -Inf
            if i==M and j<M:
                for k in range(j,M):
                    arrays[m][k]=float('-Inf')
            print arrays[m]
            
        output=[]
        for num in arrays[m-1]:
            if num>float('-Inf'):
                output.append(num)
            
        print output
    
    def zeroSumSubarray(nums):
        # Find if there is a subarray with 0 sum
        # we will sums nums one by one and use dictionary to store sums
        # if a sum us seen before then return True, cosider {1,3,5,-2,-3,6} example. 5,-2,-3 is the answer sum(1,3,5,-2,-3)=4=sum(1,3)
        dic={}
        sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            if sums==0 or nums[i]==0 or dic.has_key(sums):
                return True
            else:
                dic[sums]=1
        return False

solution=Solution()
#print solution.grayCode(2)
#print solution.lengthOfLongestSubstring("c")
#print solution.productExceptSelf([1,2,3,4])
#print solution.getPermutation(2,2)
#solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
#print solution.containsNearbyAlmostDuplicate([1,2,3,4,5], 2, 2)
print solution.nextPermutation(1234)

