class Solution:
    # @param {integer} n
    # @return {integer}
    
    def bubbleSort(self, nums):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[j]<nums[j-1]:
                    temp=nums[j]
                    nums[j]=nums[j-1]
                    nums[j-1]=temp
        return nums
    
    def mergeSort(self, nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)/2
        left=self.margeSort(nums[:mid])
        right=self.margeSort(nums[mid:])
        output=[]
        while left and right:
            if left[0]<=right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
        if left:
            output+=left
        if right:
            output+=right
        return output

    def inversions(self,nums,low,high):
        'count inversion in an array, if i<j but num[i]>num[j] then this is an inversion'
        '[2,4,1,3,5] total inversion is inversion of [2,4,1]+inversion of [3,5] and inversion of [1,2,4] and [3,5]'
        'so modified merge should work'
        
        if (high-low)<=1:
            return nums[low:high+1],0
        
        mid=(low+high)//2

        left,leftCount=self.inversions(nums,low,mid)
        right,rightCount=self.inversions(nums,mid+1,high)

        i,j=0,0
        res=[]
        count=0
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
                count+=len(left)-i
        

        if i<=len(left)-1:
            res+=left[i:]
        if j<=len(right)-1:
            res+=right[j:]

        return res,count+leftCount+rightCount


    def quicksort(self,nums, l, r):
        # get a pivot (left of pivot are samller numvbers and right is greater), recursively sort left and right of the pivot
        # Advantages: One of the fastest algorithm on average. Doesn't need additional memory i.e. it's an in-place sorting algorithm.
        # Disadvantages: Worst Case complexity is O(N^2),e.g, sorting 1,2,3,4,5
        # Comparision to Merge Sort, Merge Sort guarantee O(NlogN) time, however it requires additional memory with size N.
        # Quick Sort doesn't require additional memory but the running time is not guaranteed.

        # this gurantees the the algorithm is terminating, base case
        if l < r:
            # partition the list
            pivot = self.partition(nums, l, r)
            # sort both halves
            quicksort(nums, l, pivot-1)
            quicksort(nums, pivot+1, r)

    

    def quickSelect(self,nums,l,r,k):
        'find kth smallest in nums'
        'we are doing quicksort but just recursing one direction'
        pivot=self.partition(nums,l,r)
        if k==pivot:
            return nums[k-1]
        elif k<pivot:
            return self.quickSelect(nums,l,pivot-1,k)
        else:
            return self.quickSelect(nums,pivot+1,r,k)

    def partition(self,nums,l,r):
        index=l

        l=l+1
        while l<=r:
            # go until a larger element than pivot is found
            while l<=r and nums[l]<=nums[index]:
                l+=1
            # go until a smaller element than pivot is found 
            while l<=r and nums[r]>=nums[index]:
                r-=1
            # swap places
            if l<=r:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
        # swap right with start
        temp=nums[index]
        nums[index]=nums[r]
        nums[r]=temp
        return r


    def CountingSort(self,nums):
        # we need the range as maxs
        maxs=max(nums)
        output=[0 for i in nums]
        count=[0 for i in range(maxs+1)]
        #count how many times a number appear
        for num in nums:
            count[num]+=1
        #count[i] here represents total numbers <=i
        for i in range(1,len(count)):
            count[i]+=count[i-1]
        #if 17 numbers <=i then place i to the 16th place of the output, decrease count so that count[i] now give updated position for new a later i
        for num in nums[::-1]:
            output[count[num]-1]=num
            count[num]-=1
        return output
    
    def mySqrt(self, x):
        # find sqrt of x
        # using binary serch find mid 
        start=0
        end=x

        while start<=end:
            mid=(start+end)/2
            # if following doesn't happen then either mid is the ans/ ans is the upper half
            if mid*mid>x:
                end=mid-1
            else:
                if (mid+1)*(mid+1)>x:
                    return mid
                else:
                    start=mid+1


    def myPow(self, x, n):
        # 2^4=2^2*2^2
        if n < 0:
            return 1 / self.pow(x, -n)
        else:
            return self.pow(x, n)

    def pow(self, x, n):
        if n == 0:
            return 1

        temp = self.pow(x, n / 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x
    

        
solution=Solution()
#print solution.trailingZeroes(100)
#print solution.romanToInt('MMCCCXCIX')
#print solution.isHappy(882)
#print solution.countPrimes(100)
#print solution.isValid("[{}]")
#print solution.merge([1,0],1,[2],1)
#print(solution.countPrimes(113))
#print solution.binarySearch([2,3,4],1)
#print solution.mySqrt(1000)
#print solution.minSubArrayLen(15,[5,1,3,5,10,7,4,9,2,8])
#print solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],23)
#print solution.findMin([1,2])
#print solution.findPeakElement([1,2,3,1])
#print solution.searchMatrix1([[-5]], -2)
solution.CountingSort([2,5,3,0,2,3,0,3])
