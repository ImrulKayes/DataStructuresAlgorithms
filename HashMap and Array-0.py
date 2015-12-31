class Solution:
    def isIsomorphic(self, s, t):
        # Given two strings s and t, determine if they are isomorphic.
        # Two strings are isomorphic if the characters in s can be replaced to get t.
        dic1={}
        dic2={}

        for i in range(0,len(s)):
            # if char in s has mapping, that should be correspoding char of t,  unless no mapping possible
            if dic1.has_key(s[i]):
                if dic1[s[i]]!=t[i]:
                    return False
            else:
                # if char is s has no mapping, corresponing t should have no mapping also, map them both ways 
                if dic2.has_key(t[i]):
                    return False

                dic1[s[i]]=t[i]
                dic2[t[i]]=s[i]
        return True

    def groupAnagrams(self, strs):

        # Given an array of strings, group anagrams together.   
        if not strs:    return []

        dic={}

        output=[]

        for strVal in strs:

            dic.setdefault(''.join(sorted(strVal)),[]).append(strVal)

        for k,v in dic.iteritems():

            output.append(sorted(v))

        return output
    
    def majorityElement(self, nums):
        # Given an array of size n, find the majority element. The majority element is the element that appears more than ceil(n/2)
        # use voting, simply using number and count
        if not nums:

            return 

        num=nums[0]

        count=1

        for num1 in nums[1:]:

            if num1==num:

                count+=1

            else:

                if count>1:

                    count-=1

                else:

                    num=num1

                    count=1

        count=0

        # check whether the appears more than half
        for num1 in nums:

            if num==num1:

                count+=1

        if count>len(nums)/2:

            return num

        else:

            return
    
    def threeSum1(self, nums):
        # Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
        # assume nums is sorted. Iterate over nums, for each num find two numbsers that sums to zero using first (j) and last pointer (k) on the remaining elements.
        # j and k need to be adjusted based on the results of three elements.
        # Later we have an implementaion using 2sum (dictionaty)
        output=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                target=nums[i]+nums[j]
                # we decrement k as we know smaller numbers can only produce the zero sum
                if nums[k]+target>0:
                    k-=1
                # we increment j as we know greater numbers can only produce the zero sum
                elif nums[k]+target<0:
                    j+=1
                else:
                    if [nums[i],nums[j],nums[k]] not in output:
                        output.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
        return output

    def threeSum(self, nums):
        # sort first, for each nums find two nums from the remaining nums using 2Sum (dictionary)
        output=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            target=-nums[i]
            # now we need to get this target adding remining two nums
            dic={}
            for j in range(i+1,len(nums)):
                # our target is nums[j], if that exist then we have got an output
                # note that in each entry of dictionaty: value= this number, key= what we need more adding that with value will make the target
                # why nums[j] is the largest, because the nums are sorted, no big numbers as value didn't come before
                if dic.has_key(nums[j]):
                    if [nums[i],target-nums[j],nums[j]] not in output:
                        output.append([nums[i],target-nums[j],nums[j]])
                else:
                    dic[target-nums[j]]=nums[j]
        return output
    
    def majorityElement(self, nums):
        # Given an integer array of size n, find all elements that appear more than ceil(n/3)
        # Consider majority element of this version: You want to know if there is a value that is present in the list for more than half of the elements in that list
        # Boyer-Moore Algorithm voting alorithm (http://gregable.com/2013/10/majority-vote-algorithm-find-majority.html) could be used, we know there would be just one such element like that
        # In the first pass, we need 2 values: A candidate value, initially set to any value A count, initially set to zero.
        # For each element in our input list, we first examine the count value. If the count is equal to 0, we set the candidate to the value at the current element.
        # Next, first compare the element's value to the current candidate value. If they are the same, we increment count by 1. If they are different, we decrement count by 1.
        # A second O(N) pass can verify that the candidate is the majority element
        # The same apporach has been applied here as only two maximum majory element is possible if majority elements appear more than ceiling(n/3)
        # The essential concepts is you keep a counter for the majority number X. If you find a number Y that is not X, the current counter should deduce 1. The reason is that if there is 5 X and 4 Y, there would be one (5-4) more X than Y. This could be explained as "4 X being paired out by 4 Y"
        if len(nums)==0:
            return []        
        candidate1,candidate2,count1,count2=float('inf'),float('inf'),0,0
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
            else:
                if count1==0:
                    count1,candidate1=1,num
                elif count2==0:
                    count2,candidate2=1,num
                else:
                    count1-=1
                    count2-=1
        countCandidate1,countCandidate2=0,0
        for num in nums:
            if num==candidate1:
                countCandidate1+=1
            if num==candidate2:
                countCandidate2+=1
        output=[]
        if candidate1==candidate2:
            return [candidate1]
        if countCandidate1>int(len(nums)/3):
            output.append(candidate1)
        if countCandidate2>int(len(nums)/3):
            output.append(candidate2)
        return output                


    def threeSumClosest(self, num, target):
        # Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
        # using the same concept from 3 sum (above)
        num=sorted(num)
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                if abs(sum-target)<abs(result-target):
                    result = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result

    def fourSum1(self, nums,target):
        # this is based on 3 sum but exceeds runtime  O(n qube)
        # one problem here is the added cost due to the duplicate check
        # the solution after this doesn't do this, rather places new result wisely into the output
        output={}
        result=[]
        nums=sorted(nums)
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                k,l=j+1,len(nums)-1
                while k<l:
                    sums=nums[i]+nums[j]+nums[k]+nums[l]
                    if sums==target:
                        key=str(nums[i])+str(nums[j])+str(nums[k]),str(nums[l])
                        if not output.has_key(key):
                            output[key]=[nums[i],nums[j],nums[k],nums[l]]
                            k+=1
                            l-=1
                    elif sums>target:
                        l-=1
                    else:
                        k+=1
        for k,v in output.iteritems():
            result.append(v)
        return result

    def fourSum(self, nums, target):
        ln = len(nums)
        if ln < 4:
            return []

        ans = []
        nums.sort()

        for i in range(ln-3):
            for j in range(i+3, ln):
                m, n, add2V = i+1, j-1, nums[i] + nums[j]
                while (m < n):
                    add4V = add2V + nums[m] + nums[n]
                    if add4V == target:
                        ans.append((nums[i], nums[m], nums[n], nums[j]))
                        m += 1
                    elif add4V > target:
                        n -= 1
                    else:
                        m += 1
        return list(set(ans))

    def setZeroes1(self, matrix):
        # simple solution using O(mn) space.
        # for each entry it checks whether it was originally 0 (from temp), if it was then makes all rows and columns zero
        # we can check which column and rows would be zero by checking the matrix and keeping the numsers in two lists (one for fow and one for colum), in this case O(m+n) space
        # A constat space solution is below which uses first row and matrix to store flags(wherether corresponding row of column will be zeroed)
        m,n=len(matrix),len(matrix[0])
        temp=[[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                temp[i][j]=matrix[i][j]       
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0 and temp[i][j]==0:
                    for k in range(m):
                        matrix[k][j]=0
                    for k in range(n):
                        matrix[i][k]=0
        #print temp
        #print matrix

    def setZeroes(self, matrix):
        # Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
        # we will use first row and column to store whether corresponding rows and colums will be zero
        # first keep record whether first row or column is zero in two variables
        # then go through all elements (except first and second row), if zero then set corresponding fist row and column entry zero
        # then check first row and columns, if any zero make the corresponding columns or rows zero
        # finally make first row and colum zero checking the two variables 
        m,n=len(matrix),len(matrix[0])
        firstColumnZero,firstRowZero=False,False
        for i in range(m):
            if matrix[i][0]==0:
                firstRowZero=True

        for j in range(n):
            if matrix[0][j]==0:
                firstColumnZero=True
                  
        # make corresponding first row and first column zero
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0

        # now, set zeroes to rows and colums 
        for i in range(1,n):
            if matrix[0][i]==0:
                for j in range(1,m):
                    matrix[j][i]=0

        # set zeroes to first row and column (if applicable)
        if firstRowZero:
            for j in range(n):
                matrix[0][j]=0
        if firstColumnZero:
            for i in range(m):
                matrix[i][j]=0                
        print matrix

    def rotate(self, matrix):
        # rotate a matrix 90 degree clockwise in place
        n=len(matrix)

        # for each outer layer
        for i in range(n/2):
            # rotate all elemenets in that outer layer, at layer i=3, j=(n-1)-i rotation required, j can be used as col
            for j in range(i,(n-1-i)):

                # save the first element, matrix[i][i] is the first element 
                temp = matrix[i][j]

                #left to top
                matrix[i][j]=matrix[n-1-j][i]

                #bottom to left
                matrix[n-1-j][i]= matrix[n-1-i][n-1-j]

                #right to bottom
                matrix[n-1-i][n-1-j]= matrix[j][n-1-i]

                #save element to right
                matrix[j][n-1-i] = temp               

                   
    def spiralOrder(self, matrix):
        # appended elements from outer layer in spial order and continue
        # one fu**ing problem is array indexing, this approach is fine for an input n*n
        # but consider inputs like n*m where n=2 and m=4, or m=2 and n=4, in these cases  termination condition is required
        # only one row and only one column matix should be separately handled
        if len(matrix)==0:
            return []
        m,n=len(matrix),len(matrix[0])
        output=[]
        if m==1 and n==1:
            return [matrix[0][0]]
        if m==1:
            for i in range(n):
                output.append(matrix[0][i])
            return output
        if n==1:
            output.append(matrix[0][0])
            for i in range(1,m):
                output.append(matrix[i][0])
            return output
                

        for i in range(m):
            row,col=i,i
            maxRow,maxCol=m-i-1,n-i-1

            # if we have two rows or columns, first iteration is the result, so break
            if maxCol==0 or maxRow==0:
                break
            
            # top row
            for j in range(col,maxCol+1):
                output.append(matrix[row][j])
            # right column
            for j in range(row+1,maxRow+1):
                output.append(matrix[j][maxCol])
            # if this was the maxRow then no low portion exist
            if row!=maxRow:
                # bottom row
                for j in range(maxCol-1,col-1,-1):
                    output.append(matrix[maxRow][j])
                # left column
                for j in range(maxRow-1,row,-1):
                    output.append(matrix[j][col])
        return output

    def generateMatrix(self, n):
        # layer by layer construction
        # appended elements from outer layer in spial order and continue
        m=n
        matrix=[[1 for j in range(m)] for i in range(m)]
        if n==1:
            return matrix
        num=1
        for i in range((m/2)+1):
            rowStart,colStart=i,i
            rowEnd,colEnd=m-i-1,n-i-1
            for j in range(colStart,colEnd+1):
                matrix[rowStart][j]=num
                num+=1
            for j in range(rowStart+1,rowEnd+1):
                matrix[j][colEnd]=num
                num+=1
            for j in range(colEnd-1,colStart-1,-1):
                matrix[rowEnd][j]=num
                num+=1
            for j in range(rowEnd-1,rowStart,-1):
                matrix[j][colStart]=num
                num+=1
        return matrix


    def removeDuplicates(self, nums):
        # keep a variable to track which num has seen last and a count to track how many times
        # if count>2 pop that num from list, an index variable tracks what num to focus
        # but this solution in O(n*n) as pop in a list is O(n)
        # a better solution is below
        if len(nums)==0:
            return 0
        m=len(nums)
        index,i=0,0
        count=0
        temp=-10000000
        while i<m:
            if temp==nums[index]:
                count+=1
                if count>2:
                    nums.pop(index)
                else:
                    index+=1
            else:
                temp=nums[index]
                count=1
                index+=1
            i+=1
        return len(nums)

    def removeDuplicates(self, nums):
        # Romove duplicate from an array where duplicate are allowed at most twice, https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
        # the main idea is to used an index to build valid lists in that lists
        # index indicates list upto which is valid, so essesntially we are not concerned about the list after index.
        # the problem states It doesn't matter what you leave beyond the new length.
        # if elements that appears no more than two times are copied 
        count=1
        lenNums=len(nums)
        if lenNums<=1:
            return lenNums
        old=nums[0]
        index=1
        for i in range(1,lenNums):
            if nums[i]==old:
                count+=1
                if  count<=2:
                    nums[index]=nums[i]
                    index+=1
            else:
                count=1
                old=nums[i]
                nums[index]=nums[i]
                index+=1
        return  index
    
    def sortColors(self, nums):
        # Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
        # Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
        # concise solution below
        # if we get 0, pop it and add at first, if 1 then do pass to next, if 2 then appends at the last
        # we are beginning from first non-zero
        current=0
        lens=len(nums)
        start=0
        if len(nums)<=1:
            return
        for i in range(lens):
            if nums[i]==0:
                start+=1
            else:
                break

        current=start
        for i in range(start,lens):
            if nums[current]==0:
                a=nums.pop(current)
                nums.insert(0,a)
                current+=1
            elif nums[current]==1:
                current+=1
            else:
                a=nums.pop(current)
                nums.append(a)

    def sortColors(self, A):
        i = 0
        for j in range(len(A)):
            if A[i] == 0:
                A.insert(0, A.pop(i))
            elif A[i] == 2:
                A.append(A.pop(i))
                i -= 1
            i += 1


                    
solution=Solution()
#print solution.isIsomorphic("ab","aa")
#print solution.anagrams([])
#print solution.singleNumber([1,1,2,3,2,1,4,3])
#print solution.majorityElement([4,5,4])
#print solution.twoSum([2,7,7,15],14)
#print solution.wordBreak("leetcode",["leet","code"])
#print solution.singleNumber("1,1,1,2,3,3,3,4,4,4")
#print solution.threeSum([-5,1,4])
#print solution.majorityElement([0,0,0])
#print solution.threeSumClosest([1,1,1,0],-100)
#print solution.threeSumClosest([0,2,1,-3],1)
#print solution.fourSum([1,0,-1,0,-2,2],0)
#solution.setZeroes([[1,2,3],[4,0,5],[5,1,0]])
#solution.rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
#solution.rotate([[7,8,9],[11,12,13],[17,18,19]])
#print solution.spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])
#print solution.spiralOrder([[7],[9],[6]])
#print solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#print solution.removeDuplicates([1,1,1,2,2,2,3,4])
#solution.sortColors([0,0,1,2,1,2,0,1,2,1])
solution.generateMatrix(2)


