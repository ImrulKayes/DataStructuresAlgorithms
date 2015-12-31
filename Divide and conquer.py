class Solution:
    def maxSubArray(self, nums):
        # can be easily solved using dynamic programming. See dynamic programming section
        print self.maxSubArray(self, nums,0,len(right))
    def maxSubArray1(self,nums,low,high):
        mid=int((low+high)/2)
        if low==mid:
            return nums[low]
        else:
            left=self.maxSubArray1(nums,low,mid)
            right=self.maxSubArray1(nums,mid,high)

            sum=0
            index=mid-1
            while index>=low:
                if nums[index]>=0:
                    sum+=nums[index]
                    index-=1
                else:
                    break
            index=mid
            while index<high:
                if nums[index]>=0:
                    sum+=nums[index]
                    index+=1
                else:
                    break            
            return max(left,right,sum)
        

    def merge (self,a,b):
        output=[]
        if not a and b:
            output=b
        elif not b and a:
            output=a
        elif not a and not b:
            output=[]
        else:
            i=0
            j=0
            while i<len(a) and j<len(b):
                if a[i]<b[j]:
                    output.append(a[i])
                    i+=1
                else:
                    output.append(b[j])
                    j+=1
            if i==len(a):
                output+=b[j:len(b)]
            else:
                output+=a[i:len(a)]

        return output

    def mergeSort(self, nums):
        # just use the array rather then these high and low, see search-sort.py
        print self.mergeSort1(nums,0,len(nums)) 

    def mergeSort1(self,nums,low,high):
        mid=int((low+high)/2)
        if low==mid:
            return [nums[low]]
        else:
            a=self.mergeSort1(nums,low,mid)
            b=self.mergeSort1(nums,mid,high)
            return self.merge(a,b)

    def maxSubArray(self, nums):
        if len(nums)==0:
            return 0
        else:
            print self.maxSubArray1(nums,0,len(nums))
    def maxSubArray1(self,nums,low,high):
        mid=int((low+high)/2)
        if low==mid:
            return nums[low]
        else:
            left=self.maxSubArray1(nums,low,mid)
            right=self.maxSubArray1(nums,mid,high)

        sum=0
        maximum=-100000
        index=mid-1
        while index>=low:
            sum+=nums[index]
            if sum>=maximum:
                maximum=sum
            index-=1

        index=mid
        sum=maximum
        while index<high:
            sum+=nums[index]
            if sum>=maximum:
                maximum=sum
            index+=1
        return max(left,right,maximum)
    
        
    def largestNumber(self, nums):
        if len(nums)==0:
            return
        if len(nums)==1:
            return str(nums[0])        
        return self.largestNumber1(nums,0,len(nums)) 
    def largestNumber1(self,nums,low,high):
        mid=int((low+high)/2)
        if low==mid:
            return str(nums[low])
        else:
            a=self.largestNumber1(nums,low,mid)
            b=self.largestNumber1(nums,mid,high)
            if int(a+b)>int(b+a):
                return str(a+b)
            else:
                return str(b+a)
            
    def subsets(self, nums):
        # simple, if subset([1,2,3])= subset([1,2])+put 3 in each set of subset([1,2])
        # one thing is to note, when putting 3, each set had to make a copy, otherwise it will be inserted into the old one
        # sorted output (in a set) is expected
        if len(nums)==0:
            return [[]]
        else:
            listoflist=self.subsets(nums[:len(nums)-1])
            newlists=[]
            for lists in listoflist:
                copylist=list(lists)
                copylist.append(nums[len(nums)-1])
                newlists.append(sorted(copylist))
            listoflist=listoflist+newlists
            return listoflist
    def subsetsWithDup(self, nums):
        if len(nums)==0:
            return [[]]        
        lists=self.subsets(nums)
        dic={}
        for x in lists:
            dic[''.join(str(x))]=x
        output=[]
        for k,v in dic.iteritems():
            output.append(v)
        return output
            
    def generate(self, numRows):
        #pascal's triangle
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        else:
            listoflist=self.generate(numRows-1)

            if numRows==2:
                listoflist.append([1,1])
                return listoflist
            # if more than two rows, add consequtive elements from the last row
            lastRow=listoflist[len(listoflist)-1]
            newRow=[1]

            for i in range(len(lastRow)-1):
                newRow.append(lastRow[i]+lastRow[i+1])
            newRow.append(1)
            listoflist.append(newRow)
            return listoflist
            
    def getRow(self, numRows):
        #pascal's triangle
        if numRows==0:
            return [1]
        if numRows==1:
            return [1,1]
    
        lists=self.getRow(numRows-1)
        # if more than two rows, add consequtive elements from the last row
        lastRow=lists
        newRow=[1]
        for i in range(len(lastRow)-1):
            newRow.append(lastRow[i]+lastRow[i+1])
        newRow.append(1)

        return newRow
    def generateParenthesis(self, n):
        # consider if we have only () where we can put another ()---->begining ()(), last ()(), at occurence before ) (()), then from all these we have to take those unique ones
        if n==0:
            return None
        if n==1:
            return ["()"]
        lists=self.generateParenthesis(n-1)
        newlists=[]
        for element in lists:
            element1=list(element)
            element2=list(element)
            element3=list(element)
            
            element2.insert(0,'()')
            b=''.join(element2)

            element3.append('()')
            c=''.join(element3)
            newlists.append(b)
            newlists.append(c)

            for i in range(len(element)):
                temp=list(element)
                if element[i]==')':
                    temp.insert(i,'()')
                    newlists.append(''.join(temp))
        # get unique ones
        dic={}
        returnlist=[]
        for x in newlists:
            dic[x]=1
        for k,v in dic.iteritems():
            returnlist.append(k)

        return returnlist




    def letterCombinations(self, digits):
        # intuitive, for 2 output ['a','b','c'], for 23 insert each of "def" for 3 into all of output of 2, do for all digits using recursion
        dic={1:"00",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if len(digits)==0:
            return []
        if len(digits)==1:
            return list(dic[int(digits[0])])
        else:
            lists=self.letterCombinations(digits[:len(digits)-1])
            chars=dic[int(digits[len(digits)-1])]
            output=[]
            for char in chars:
                for element in lists:
                    output.append(element+char)
            return output

    def getPermutation(self, n, k):
        nums=[]
        for i in range(1,n+1):
            nums.append(str(i))
        lists=self.permute(nums)
        #output=[]
        #for x in lists:
 #           output.append(int(''.join(x)))
 #       sortedOutput=sorted(output)

        print lists
 #       if k>len(sortedOutput):
#            return
#        return sortedOutput[k-1]
        
    def permute(self, nums):
        # for [1,2,3], put 3 to all places of permuation results of [1,2]
        if len(nums)==1:
            return [[nums[0]]]
        else:
            list1=self.permute(nums[0:len(nums)-1])
            output=[]
            for element in list1:
                temp=list(element)
                for i in range(0,len(element)+1):
                    temp.insert(i,nums[len(nums)-1])
                    #x=''.join(temp)
                    #print x
                    x=list(temp)
                    x=sorted(x)
                    output.append(''.join(x))
                    temp=list(element)
            return output        

        

solution=Solution()
#solution.mergeSort([5,4,3,2,10,3,51])
#solution.mergeSort([5,4,3,2,10,3,51])
#solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#print solution.permute([1,2,3])
#print solution.getPermutation(2,2)
#print solution.largestNumber(sorted([10,2,3]))
#print solution.generate(0)

#print solution.getRow(3)
#print solution.generateParenthesis(4)
#print solution.subsetsWithDup([1,2,2])
#print solution.combine(5,3)
#print len(solution.letterCombinations("234"))
#solution.getPermutation(3,2)

