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

    def quicksort(myList, start, end):
        # get a pivot (left of pivot are samller numvbers and right is greater), recursively sort left and right of the pivot
        # Advantages: One of the fastest algorithm on average. Doesn't need additional memory i.e. it's an in-place sorting algorithm.
        # Disadvantages: Worst Case complexity is O(N^2),e.g, sorting 1,2,3,4,5
        # Comparision to Merge Sort, Merge Sort guarantee O(NlogN) time, however it requires additional memory with size N.
        # Quick Sort doesn't require additional memory but the running time is not guaranteed.

        # this gurantees the the algorithm is terminating, base case
        if start < end:
            # partition the list
            pivot = partition(myList, start, end)
            # sort both halves
            quicksort(myList, start, pivot-1)
            quicksort(myList, pivot+1, end)
        return myList
    

    def partition(myList, start, end):
        pivot = myList[start]
        left = start+1
        right = end
        done = False
        while not done:
            # go until a larger element than pivot is found 
            while left <= right and myList[left] <= pivot:
                left = left + 1
                
            # go until a smaller element than pivot is found 
            while myList[right] >= pivot and right >=left:
                right = right -1

            if right < left:
                done= True
            else:
                # swap places
                temp=myList[left]
                myList[left]=myList[right]
                myList[right]=temp

        # swap start with myList[right]
        temp=myList[start]
        myList[start]=myList[right]
        myList[right]=temp
        return right

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
