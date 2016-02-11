class Solution:
    # @param {integer} n
    # @return {integer}
    
    'Recursive Binary search: using varying array size'
    def BinarySearch(self, nums,target):
        if len(nums)==0:
            return False
        mid=int(len(nums)/2)
        if target<nums[mid]:
            return self.BinarySearch(nums[:mid],target)
        elif target>nums[mid]:
            return self.BinarySearch(nums[mid:],target)
        else:
            return True
        
    'Recursive Binary search: using varying indexes'
    'always note that l says left index and r says right index, l<=r means we have at least one element'
    def binarySearch(self, nums,l, r,target):

        if l>r:
            return False
        mid=(l+r)/2
        if nums[mid]==target:
            return True
        if target<nums[mid]:
            return self.binarySearch(nums,l,mid-1,target)
        else:
            return self.binarySearch(nums,mid+1,r,target)

    'Iterative Binary search: using varying array indexes'
    'what conditions it fails? when target< nums, target>nums, target within the nums range but not present'
    'in those cases l>r, either l gives 0 or >0, l denotes first number greater than target'
    'In binary search if element is not found and if low>0, then low will give the index of the element just'
    'greater than the target, so if low=0 then all elements are greater than target. Say 10,20,30,40 finding 0 will give low=0, finding 50 will give low=4, finding 32 will give low=3.'
    
    def binarySearch(self, nums,target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)/2
            if nums[mid]==target:
                return True
            if target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        return False

    def searchRange(self, nums, target):
        """
        Given a sorted array of integers, find the starting and ending position of a given target value.
        [1,2,3,3,3,4,5] and target=3 will return [2,4]
        """
        if not nums:    return [-1,-1]
        
        low,high=0,len(nums)-1
        
        while low<=high:
            mid=(low+high)/2
            if target>nums[mid]:
                low=mid+1
            elif target<nums[mid]:
                high=mid-1
            else:
                start,end=mid,mid
                while start>=0 and nums[mid]==nums[start]:
                    start-=1
                while end<=len(nums)-1 and nums[mid]==nums[end]:
                    end+=1
                return [start+1,end-1]
        return [-1,-1]


    def firstBadVersion(self, n):
        """
        n versions, find the first bad version https://leetcode.com/problems/first-bad-version/
        bad is definately there
        """
        if n <= 1:
            return n
        front = 1
        end = n
        while front < end:
            middle = (front + end)//2
            'if mid is bad then results in the left including middle'
            if isBadVersion(middle):
                end = middle
            'if mid is good then result is in the right side'
            else:
                front = middle + 1
        return front
    
    def firstBadVersion(self, n):
        if n == 0:
            return 0
        return self.search(1, n)

    def search(self, l, r):
        mid = (l+r)//2
        if isBadVersion(mid):
            r = mid - 1
            'if mid is bad and before the mid is good then mid is the answer, else search left of the mid'
            if not isBadVersion(r):
                return mid
            else:
                return self.search(l, r)
        else:
            'if mid is good and the next of mid is bad then next is the answer, else search right'
            l = mid + 1
            if isBadVersion(l):
                return l
            else:
                return self.search(l, r)

    def searchMaxIncreasingDecreasing(self,nums):
        "Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array. 8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1 will return 500"
        "compare the mid with left and right element"
        
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)/2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return nums[mid]
            elif nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid-1

            
    def magicIndex(self,nums):
        # return i if nums[i]==i, where nums is sorted
        # easy, using binary search, but if duplicate num exists then modification required
        if not  nums:
            return -1
        mid=len(nums)/2
        if nums[mid]==mid:
            return mid

        # if mid number is less than mid index, then after mid number'th index element are not magic (as indexes are larger and elements are at most mid),
        # so recursing left until min(mid-1, nums[mid]) 
        if nums[mid]<mid:
            leftIndex=min(mid-1, nums[mid])
            left=self.magicIndex(nums[:leftIndex+1])
            if left>=0:
                return left
        # also recurse right
        if nums[mid]>mid:
            rightIndex=max(mid+1, nums[mid])
            right=self.magicIndex(nums[rightIndex:])
            if right>=0:
                return right 


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

    def searchMatrix1(self, matrix, target):
        # this is O(nlogm) solution, for each row we are doing binary search, a better O(logn+logm) solution is below
        rows,cols=len(matrix),len(matrix[0])
        for i in range(rows):
            low,high=0,cols-1
            while low<=high:
                mid=(low+high)/2
                if matrix[i][mid]==target:
                    return True
                else:
                    if target<matrix[i][mid]:
                        high=mid-1
                    else:
                        low=mid+1
        return False

    def searchMatrix(self, matrix, target):
        # easy!, two binary search, first through all first columns to get which row might have the number
        # then another binary search to that row to get the element
        # low in first search gives the index who has greater value than the target, so basically we have to search previous row

        low = 0
        high = len(matrix)-1
        while low<=high:
            midpoint = (low + high)//2
            if matrix[midpoint][0] == target:
                return True
            else:
                if target < matrix[midpoint][0]:
                    high = midpoint-1
                else:
                    low = midpoint+1

        if low>0:
            i=low-1
        else:
            i=low

        low,high=0,len(matrix[0])-1
        while low<=high:
            midpoint = (low + high)//2
            if matrix[i][midpoint] == target:
                return True
            else:
                if target < matrix[i][midpoint]:
                    high = midpoint-1
                else:
                    low = midpoint+1
        return False

    def searchMatrix1(self, matrix, target):
        # This also simple, based on previous searchMatrix
        # we start with first column an find a 'low' (next line), then we have to search only low number of rows for a search starting at second line and the process will continue
        # low in first search gives the index who has greater value than the target, so basically we have to search previous row

        main=matrix
        m,n=len(matrix),len(matrix[0])
        for j in range(n):        
            low = 0
            high = m-1
            while low<=high:
                midpoint = (low + high)//2
                if matrix[midpoint][j] == target:
                    return True
                else:
                    if target < matrix[midpoint][j]:
                        high = midpoint-1
                    else:
                        low = midpoint+1

            if low>0:
                i=low-1
            else:
                i=low
            #print i
            m=i+1
        return False


    def findMin(self, nums):
    #Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). Find the minimum element.You may assume no duplicate exists in the array.
    #This problems seems like a binary search, and the key is how to break the array to two parts, so that we only need to work on half of the array each time, i.e.,when to select the left half and when to select the right half.
    #If we pick the middle element, we can compare the middle element with the left-end element. If middle is less than leftmost, the left half should be selected; if the middle is greater than the leftmost, the right half should be selected. Using simple recursion, this problem can be solve in time log(n).
    #In addition, in any rotated sorted array, the rightmost element should be less than the left-most element, otherwise, the sorted array is not rotated and we can simply pick the leftmost element as the minimum.

        l = len(nums)-1 
        if l==0:
            return nums[0]
        mid = l/2

        if nums[mid]<nums[0]:
            # right side is sorted, so rotation has been done on leftside, so exclude first element and include mid and search there
            return self.findMin(nums[1:mid+1])  
        else:
            return self.findMin(nums[mid+1:])

    def search(self, nums, target):
        # search is  a rotated sorted array, when duplicates are allowed
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target:
                return True
            # if left is sorted, then target might be there if inside, or target in other side
            if nums[left]<nums[mid]:
                if nums[left]<=target and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            # if right is sorted, then target might be there if inside or target in other side
            elif nums[left]>nums[mid]:
                if nums[mid]<target and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            # else, we have one element left and that is not equal to target
            else:
                left+=1
        return False


    def findPeakElement(self, nums):
        # A peak element is an element that is greater than its neighbors. Given an array nums with nums[i]!=nums[i+1],num[-1]=num[n]=-inf find a peak element and return its index. e.g. [1,2,3,1] 3 is a peak element and your function should return the index number 2.
        # The array may contain multiple peaks, in that case return the index to any one of the peaks is fine. 

        # binary search, if mid is less than mid-1 then serach in left, else search right
        # we always will get a peak in either side, if we were to get a global peak then binary search will not work
        
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if low==high:
                return low

            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid-1
        
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
#solution.numIslands([])
#solution.numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])
#solution.solve([['X','X','X','X'],['X','0','0','X'],['X','X','0','X'],['X','0','X','X']])
#solution.solve([['X','X','X'],['X','0','X'],['X','X','X']])
solution.CountingSort([2,5,3,0,2,3,0,3])
