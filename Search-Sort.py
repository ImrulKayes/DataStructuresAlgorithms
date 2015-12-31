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
    
    def BinarySearch1(self, nums,target):

        if len(nums)==0:
            return False
        mid=int(len(nums)/2)
        if target<nums[mid]:
            return self.BinarySearch(nums[0:mid],target)
        elif target>nums[mid]:
            return self.BinarySearch(nums[mid:len(nums)],target)
        else:
            return True

    def binarySearch(self,alist, item):
        first = 0
        last = len(alist)-1
        while first<=last:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                return True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return False

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
            # if following doesn't happen then either mid is the ans/ ans is the lower half
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

    
    def numIslands(self, grid):
        # Given a 2d grid map of 1's (land) and '0's (water) count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        # (You may assume all four edges of the grid are all surrounded by water.)
        
        # island is connected vertically and horizontally 1s with four sides 0s
        # for each grid if we get 1 then will count++ and make all adjacent 1's (four) 0, recursively
        # this solution could be thought as a BFS
        # if no grid or one row or one column  then no island

        if not grid or len(grid)==0 or len(grid[0])==0:
            return 0
        
        m,n=len(grid),len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    count+=1
                    self.margeGrid(grid,i,j)

        return count
    def margeGrid(self,grid,i,j):
        m,n=len(grid),len(grid[0])
        if i<0 or j<0 or i>=m or j>=n:
            return
        if grid[i][j]==0:
            return
        
        #this element was 1, so make it 0 (visited)
        grid[i][j]=0
        self.margeGrid(grid,i+1,j)
        self.margeGrid(grid,i-1,j)
        self.margeGrid(grid,i,j+1)        
        self.margeGrid(grid,i,j-1) 

    def solve(self, board):
        # Given a 2D board containing X and 0, capture regions surrounded by X, A region is captured by flipping all 0s into Xs in that surrounded region.
        # https://leetcode.com/problems/surrounded-regions/
        
        # this solution is based on numIslands
        # if an element is 0 then recusively check all four adjacent elements, if they are not X then 0 should remain 0, otherwise make it X
        # another easy solution is here https://leetcode.com/discuss/42445/a-really-simple-and-readable-c-solution%EF%BC%8Conly-cost-12ms
        # First, check the four border of the matrix. If there is a element is 'O', alter it and all its neighbor 'O' elements to '1'.
        # Then ,alter all the 'O' to 'X'
        # At last,alter all the '1' to 'O'
        if not board or len(board)==0 or len(board[0])==0:
            return
        m,n=len(board),len(board[0])
        count=0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j]=='0':
                    x=self.margeBoard(board,i,j)
                    
        print board

    def margeBoard(self,board,i,j):
        m,n=len(board),len(board[0])
        #only a boundary element is 0 then it will remain 0 and all neightbours of it will remain 0 (so returning false) 
        if i==0 or j==0 or i==m-1 or j==n-1:
            if board[i][j]=='0':
                return False
        # make the 0 element X, we will later change it if all four negighbours are not 0
        board[i][j]='X'

        # if all four neighbors are X then return True
        if board[i+1][j]=='X' and board[i-1][j]=='X' and board[i][j+1]=='X' and board[i][j-1]=='X':
            return True

        # recrusively check the neighbors 
        a=b=c=d=True
        if board[i+1][j]=='0':
            a=self.margeBoard(board,i+1,j)
        if board[i-1][j]=='0':
            b=self.margeBoard(board,i-1,j)
        if board[i][j+1]=='0':
            c=self.margeBoard(board,i,j+1)            
        if board[i][j-1]=='0':
            d=self.margeBoard(board,i,j-1) 
        if a and b and c and d:
            return
        else:
            # if any of the neighbors is not X then this element should remain 0
            board[i][j]=='0'
            return 
        
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
