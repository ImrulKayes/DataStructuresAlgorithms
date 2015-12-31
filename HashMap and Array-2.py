class Solution:
    def findSubArray(self,nums,target):
        # In an Array, find the Contiguous Subarray with Sum to a Given Value.
        # keep two pointers, increse front if more elements needed, adjust tail if sum is greater
        
        if not nums:    return []
        head,tail=0,0
        currSum=0
        while head<len(nums):
            if currSum==target:
                return nums[tail:head]
            elif currSum>target:
                currSum-=nums[tail]
                tail+=1
            else:
                currSum+=nums[head]
                head+=1
        return []
            
    def nextGreaterElement(self,nums):
        # Given an array, print the Next Greater Element (NGE) for every element.
        # The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.
        # solution: push first element in a stack, for rest of the element if the element is geater than top of the stack pop all of the elements that are smaller, for them the element in the next greater
        # otherwise push the element in the stack, finally the elements remain in the stack have no next, so set -1 in output
        
        if not nums:    return
        q=[nums[0]]
        for i in range(1,len(nums)):
            next=nums[i]
            if q:
                if q[-1]<next:
                    print q[-1],next
                    q.pop()
                    while q and q[-1]<next:
                        print q[-1],next
                        q.pop()
                    q.append(next)
                else:
                    q.append(next)
            else:
                q.append(next)
        if q:
            for num in q:
                print num,-1
                
    def canPair(self,nums,k):
        # Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.

        # If length of given array is odd or none, return false. An odd length array cannot be divided in pairs.
        if not nums or len(nums)%2==1:
            return False
        freq={}

        # count number of unique reminders
        for num in nums:
            if freq.has_key(num%k):
                freq[num%k]+=1
            else:
                freq[num%k]=1

        for num in nums:
            rem=num%k
            # if reminder is half k, then should be even (e.g., consider 5,5,5,5 and k=10)
            if rem==k/2:
                if freq[rem]%2!=0:
                    return False
            # otherwise 
            elif freq[rem]!=freq[k-rem]:
                return False
            else:
                pass
        return True
    
    def minDist(self,nums,x,y):
        # http://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/
        # Given an unsorted array arr[] and two numbers x and y, find the minimum distance between x and y in arr[].
        # The array might also contain duplicates. You may assume that both x and y are different and present in arr[].
        if not nums:    return
        mindist='Inf'
        prev='Inf'

        #Find the first occurence of any of the two numbers (x or y) and store the index of this occurence in prev
        for i in range(len(nums)):
            if nums[i]==x or nums[i]==y:
                prev=i
                break
        #Traverse after the first occurence
        for j in range(i,len(nums)):
            #If the current element matches with any of the two then
            #check if current element and prev element are different
            #Also check if this value is smaller than minimm distance so far
            if nums[j]==x or nums[j]==y:
                if nums[j]!=nums[prev] and (j-prev)<mindist:
                    mindist=j-prev
                    prev=j
                else:
                    prev=j
        return mindist

    def segNums(self,nums):
        # You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array. Traverse array only once.
        if len(nums)==0 or len(nums)==1:
            return
        low,high=0,len(nums)-1

        while low<high:

            # Increment left index while we see 0 at left
            while nums[low]!=1 and low<high:
                low+=1
            # Decrement right index while we see 1 at right
            while nums[high]!=0 and low<high:
                high-=1

            # If left is smaller than right then there is a 1 at left and a 0 at right.  Exchange nums[high] and arr[row]
            if low<high:
                nums[low]=0
                nums[high]=1
                low+=1
                high-=1
        return nums
    
    def minSubArrayLen(self, s, nums):
        b=sorted(nums)
        print b
        sum=0
        count=0

        for i in xrange(len(b)-1,-1,-1):
            sum+=nums[i]
            count+=1
            if sum>=s:
                return count
        return 0

    # also try to solve it by DP
    def minSubArrayLen(self, s, nums):
        # given n positive numbers and s, find min length subarry such that sums>=s
        # keep two pointers, current one adds new element, if sums>=s adjust minLength by incrementing first pointer to the nextest element where also sums>=s 
        minLen, total, start = len(nums) + 1, 0, 0
        for i in range(len(nums)):
            total += nums[i]
            while total >=  s:
                minLen, total, start = min(i - start + 1, minLen), total - nums[start], start + 1
        return 0 if minLen > len(nums) else minLen            
        
solution=Solution()
#print solution.findSubArray([25, 12, 14, 22, 19, 15, 10, 23],55)
#solution.nextGreaterElement([11, 13, 21, 3])
#print solution.canPair([92, 75, 65, 48, 45, 35],10)
#print solution.minDist([3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3],3,6)
#print solution.segNums([0, 1, 0, 1, 1, 1])

def hightestWaster(nums):
    #Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
    # for each bar calculate higher left and right bar including itself
    # water trapper in a num is equal to min(left[i],right[i])-nums[i]
    
    left=[nums[i] for i in range(len(nums))]
    right=[nums[i] for i in range(len(nums))]
    for i in range(1,len(nums)):
        left[i]=max(left[i-1],nums[i])
    for i in range(len(nums)-2,-1,-1):
        right[i]=max(right[i+1],nums[i])
    waterVolume=0
    for i in range(len(nums)):
        waterVolume+=min(left[i],right[i])-nums[i]
    return waterVolume

#print hightestWaster([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])


