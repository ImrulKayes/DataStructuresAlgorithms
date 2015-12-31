#recursion and memoization are used to solve DP problems but they are totally separate things.
#And divide and conquer problems differ from DP in that the sub-problems do not overlap.
#Divide-&-conquer works best when all subproblems are independent. So, pick partition that makes algorithm most efficient & simply combine solutions to solve entire problem.
#In dynamic approach, we dont know where to partition the problem, because if we do, solution(left)+solution(right)!=solution(entire)
#dynamic programming automatically solves every subproblem that could conceivably be needed, while memoization only ends up solving the ones that are actually used.
# For instance, suppose that W and all the weights wi are multiples of 100. Then a subproblem K(w) is useless if 100 does not div
#Knapsack is a good example to understand difference DP vs recursion+memoization
#Must to do: http://people.cs.clemson.edu/~bcdean/dp_practice/

class Solution:
    def minDistance(self, word1, word2):
        # if eiter one exist, penalty=length (need to insert all chars) 
        # set zero rows and colums of the metric, penalty=lenth of the word if other dont exist
        matrix = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(word1)+1):
            matrix[i][0]=i
        for j in range(len(word2)+1):
            matrix[0][j]=j

        for i in range (1,len(word1)+1):
            for j in range(1,len(word2)+1):
                # if two chars are the same penalty is 1, else 0
                cost=1
                if word1[i-1]==word2[j-1]:
                    cost=0
                # result will be minimum of either including any of the char to the solution (1+matrix[i-1][j],1+matrix[i][j-1]) or including none (cost+matrix[i-1][j-1])
                matrix[i][j]=min(1+matrix[i-1][j],1+matrix[i][j-1],cost+matrix[i-1][j-1])

        return matrix[len(word1)][len(word2)]

    def knapsack01(self,Values,Weight,W):
        #  A thief robbing a store and can carry a maximal weight of W into their knapsack. There are n items and ith  item weigh wi and is worth vi dollars. What items should thief take?
        #  we will use K(i,w) to denote what is maximum value with i items and w weights, so k[len(values)][W] is the answer
        m,n = len(Values), W
        K = [[0 for i in range(n+1)] for j in range(m+1)]  # note this, it's a K[m][n] matrix
        for i in range(1,m+1):
            for j in range(1,n+1):
                # consider i items, if i'th items (that means W[i-1] weight) have greater value than what to fill (j) then j fill have to be done i-1  items
                if Weight[i-1]>j:   
                    K[i][j]=K[i-1][j]
                # otherwise max values including or excluding i'th item
                else:
                    K[i][j]=max(K[i-1][j],Values[i-1]+K[i-1][j-Weight[i-1]])
        return K[m][n]

    def coinChange(self,nums,coins):
        # Given a set of coins and a num, what is the minimum number of coins required to change the num
        # coins are repeated
        # let m(i) is the minimum coins possible to change i
        # for each nums from 0 to nums, if j is a coin that is less than the number then total min(1+M[j-number]) coins is the smallest number of coins, M[j-number] will be aleary calculated
        M=[-1 for i in range(nums+1)]   # or initize M with big numbers e.g., M=[0]+[nums+1]*nums, here M[1]=num+1 which indicates no coin change is possible
        M[0]=0
        for i in range(1,nums+1):
            output=[]
            for j in range(len(coins)):
                if i>=coins[j]:
                    # if change of i-coins[j] is possible
                    if M[i-coins[j]]>-1:                # or we can simply use M[i]=min(M[i],M[i-coins[j]])
                        output.append(1+M[i-coins[j]])
            # if any change possible then take the min one
            M[i]=min(output) if output else -1         # or we can just check if M[num] is num+1 in this case no change is possible for num
        return M.pop()

    def coinChange1(self, coins, amount):
        # Given a set of coins and a num, what is the minimum number of coins required to change the num
        # coins are repeated. If coins are single in the following program use M[i-coins[j-1]][j-1] rather than M[i-coins[j-1]][j] 
        # let M[i,j] is minimum coins when we have i amount and j coins
        # a recursive solution is below
        M=[[0 for j in range(len(coins)+1)] for i in range(amount+1)]

        # an amoung couldn't be changed with 0 coins, set -1
        for i in range(1,amount+1):
            M[i][0]=-1
                
        row,col=amount+1,len(coins)+1
        for i in range(1,row):
            for j in range(1,col):
                # if amount greater than current coin, two cases: either include the coin to the solution or exclude
                if i>=coins[j-1]:
                    # if include the coin then check whether two options are possible or not (e.g., both are -1)
                    if M[i-coins[j-1]][j]==-1 and M[i][j-1]==-1:
                        M[i][j]=-1
                    if M[i-coins[j-1]][j]>-1 and M[i][j-1]>-1:
                        M[i][j]=min(1+M[i-coins[j-1]][j],M[i][j-1])
                    else:
                        M[i][j]= 1+M[i-coins[j-1]][j] if M[i][j-1]==-1 else M[i][j-1]
                #otherwise, we cant include the coin 
                else:
                    M[i][j]=M[i][j-1]
        return M[row-1][col-1]

    def MakingChange1(self,num,coins):
        # coins are sorted in descending order,
        # if you want to make memoization, a matrix with num*colums is required. A special value might say whether a cell has been computed yet. 
        if num<0:
            return -1
        if num==0:
            return 0
        # in num is larger than first coin then 1+self.MakingChange(num-coins[0],coins) is answer if exist
        if num>=coins[0]:
            if self.MakingChange(num-coins[0],coins)>-1:
                return 1+self.MakingChange(num-coins[0],coins)
            else:
                return -1
        # otherwise self.MakingChange(num,coins[1:]) is the answer
        else:
            return self.MakingChange(num,coins[1:])


    def coinChange(self,coins,target):
        # how many total ways coin change possible
        # M[i,j] = total ways when we have i amount and j coins
        M=[[0 for j in range(len(coins)+1)] for i in range(target+1)]

        # zero amoung could be changed with 1 possible ways for each coins
        for j in range(len(coins)+1):
            M[0][j]=1
                

        row,col=target+1,len(coins)+1
        for i in range(1,row):
            for j in range(1,col):
                # if amount greater than current coin, two cases: either include the coin to the solution or exclude
                if i>=coins[j-1]:
                    M[i][j]=M[i-coins[j-1]][j]+M[i][j-1]
                #otherwise, we cant include the coin 
                else:
                    M[i][j]=M[i][j-1]
        print M



    def rob(self, nums):
        # line of houses, each have a value, adjacent houses are connected, get maximum ammount from the houses without getting values from two cosequtive
        # let v[i] is maximum value we can get with i nums
        
        if not nums:    return 0

        if len(nums)<=2:

            return max(nums)
        
        for i in range(2,len(nums)):

            # for i'th nums, we can either take it or not
            v[i]=max(nums[i]+v[i-2],v[i-1])

        return v[len(nums)-1] 

    def rob2(self, nums):
        # previos problem, but all houses are arranged in a circle
        # There are two cases, if we do not rob house[n], we can rob nums[:n-1] else we can rob nums[1:n-2]
        if not nums: return 0

        if len(nums)<=3:

            return max(nums)

        return max(nums[len(nums)-1]+self.rob1(nums[1:len(nums)-2]),self.rob1(nums[:len(nums)-1]))

    def climbStairs(self, n):
        # You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        # let v[i] is the number of ways to reach at i'th steps
        if n<2:
           return 1
        if n==2:
            return 2

        v=[0 for i in range(n+1)]
        v[0]=0
        v[1]=1
        v[2]=2
        # can reach from either previos or previous previous stairs
        for i in range(3,n+1):
            v[i]=v[i-1]+v[i-2]
        return v[n]

    def uniquePaths(self, m, n):
        # A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below). The robot can only move either down or right at any point in time.
        # The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).How many possible unique paths are there?

        # let K[i][j] is the number of ways a robot can reach in i-1,j-1 th grid
        # in a cell it can come from  either [i-1][j] or [i][j-1] cells
        # however in first row or colum it can go only one way as for those it can come from up (for first colums) or left (for first rows)
        if m==0 or n==0:
            return 1
        # setting all in all the cells (so, first row and colum need to be set separately)
        K=[[1 for i in range(n)] for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                K[i][j]=K[i-1][j]+K[i][j-1]
        return K[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        # Follow up for "Unique Paths": Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle is marked as 1 or 0 in the grid
        # similar to thre uniquePaths problems with some minor changes
        # in a cell it can come from  either [i-1][j] or [i][j-1] cells
        # however in first row or colum it can go only one way as for those it can come from up (for first colums) or left (for first rows), but if there is an obstacle all remaining (including that) wil be zero
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        grid=[[0 for j in range(n)] for i in range(m)]

        # for first row and column if obstacle then later cells are not accessible
        for i in range(m):
            if obstacleGrid[i][0]==0:
                grid[i][0]=1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]==0:
                grid[0][j]=1
            else:
                break
        # only one row or colum, finally we return grid[m-1][n-1], so we need special handling for 1 row and 1 col
        if m==1:
            return grid[0][n-1]
        if n==1:
            return grid[m-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                # if obostacke then no way to go there
                grid[i][j]=grid[i-1][j]+grid[i][j-1] if obstacleGrid[i][j]==0 else 0
        return grid[m-1][n-1]

    def minPathSum(self, grid):
        # Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
        # Note: You can only move either down or right at any point in time.
        # same concept with the previous one
        m,n=len(grid),len(grid[0])

        for i in range(1,m):
            grid[i][0]+=grid[i-1][0]

        for j in range(1,n):
            grid[0][j]+=grid[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]

    def maxProduct(self, nums):
        # Find the contiguous subarray within an array (containing at least one number) which has the largest product. (number can be negative)

        # let max(i) and min(i) is the maximum and minimum product respectively when we have i elements
        # maximum product can also be obtained by minimum (negative) product ending with the previous element multiplied by this element
        # so we will keep max and min for each element
        if not nums:    return 

        maxs=[x for x in nums]
        mins=[x for x in nums]
        
        for i in range(1,len(nums)):
            if nums[i]>=0:
                maxs[i]=max(nums[i],maxs[i-1]*nums[i])
                mins[i]=min(nums[i],mins[i-1]*nums[i])
            else:
                maxs[i]=max(nums[i],mins[i-1]*nums[i])
                mins[i]=min(nums[i],maxs[i-1]*nums[i])

        return max(maxs)
    
    def maximumValueContiguousSubsequence(self,nums):
        # this is also maxium subarry problem but here output is all the indexes
        # for i'the element it will be included in previous solution having i-1 elements or a new solution has to be started from here
        output=[0 for i in range(len(nums))]
        parent=[0 for i in range(len(nums))]
        output[0]=nums[0]
        parent[0]=0
        for i in range(1,len(nums)):
            if output[i-1]+nums[i]>nums[i]:
                output[i]=output[i-1]+nums[i]
                parent[i]=i-1
            else:
                output[i]=nums[i]
                parent[i]=i
        currentIndex=output.index(max(output))

        # this one is for processing output
        indexList=[]
        while currentIndex!= parent[currentIndex]:
            indexList.append(currentIndex)
            currentIndex=parent[currentIndex]
        indexList.append(currentIndex)
        print indexList[::-1]

    def maxSubArray(self, nums):

        # Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
        # let output[i] is the maxium subarry sum with i+1 elements
        # for the i'th element it will be included in previous solution having i-1 elements or a new solution has to be started from here
        if not nums:    return 

        
        output=[0 for i in range(len(nums))]
        output[0]=nums[0]

        for i in range(1,len(nums)):
            output[i]=output[i-1]+nums[i] if output[i-1]+nums[i]>nums[i] else nums[i]
        return max(output)
    
    def LongestIncreasingSubsequence(self,nums):
        # for longest increasing subsequence ending at j, we want to extent some (max) subsequece ending at in index i, i<j if j'th element is larger then i'th and add 1 for the j'th element
        # Another similar problem: consider a 2-D map with a horizontal river passing through its center. There are n cities on the southern bank with x-coordinates a(1) ... a(n) and n cities on the northern bank with
        # x-coordinates b(1) ... b(n). You want to connect as many north-south pairs of cities as possible with bridges such that no two bridges cross. When connecting cities,
        # you can only connect city i on the northern bank to city i on the southern bank.
        # solution of this: http://people.cs.clemson.edu/~bcdean/dp_practice/dp_6.swf
        # box stacking is also LIS http://people.cs.clemson.edu/~bcdean/dp_practice/dp_5.swf
        
        if not nums:    return 0       

        M=[0 for i in range(len(nums))]

        M[0]=1

        for i in range(1,len(nums)):
            maxs=0


            for j in range(0,i):

                if nums[i]>nums[j]:

                    if M[j]>maxs:

                        maxs=M[j] 

            M[i]=maxs+1

        return max(M)


    def minimumTotal(self, triangle):
        #Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
        #for a given row [1,2,3], M[first/last]=this row first/last+ previous row fast/last. M[other element]=element+ min(previous row's this and left element)  
        #finally the min in the last row is the output
        # in this solution we are using O(n*n) space, if we want to keep the traiangle intact, a less extra space solution is O(n) if we do the comuputation from bottom to up
        # in that case we need an array size with max row len of the traingle and we row by row from bottom to the up top, calculate the minimum value to each point. we just use one array to "remember" what is the minimum total value to each point from bottom.
        
        m=len(triangle)
        if m==0:    return
        if m==1: return triangle[0][0]
        for i in range(1,m):
            triangle[i][0]+=triangle[i-1][0]
            triangle[i][len(triangle[i])-1]+=triangle[i-1][len(triangle[i-1])-1]
            for j in range(1,len(triangle[i])-1):
                triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[m-1])


    def wordBreak(self, s, wordDict):
        # Given a string s and a dictionary of words dict (a list of words), determine if s can be segmented into a space-separated sequence of one or more dictionary words.
        # let status[i] is true/false if first i+1 of s could be built/not from the wordDict
        # consider "leetcode" as s, status[i]=True if s(0--i) is in the dictionary, else False.
        #s(0--i) is in dictionary is s(0--i) in dictionary of s(0..j),s(j+1...i) both in dictionary)
        
        if not s:   return True
        status=[0 for i in range(len(s))]
        if s[0] in wordDict:
            status[0]=True
        for i in range(1,len(s)):
            # if the whole word upto is in the dictionary
            if s[:i+1] in wordDict:
                status[i]=True
            # else determine whether we can build it
            else:
                for j in range(i):
                    if status[j] and s[j+1:i+1] in wordDict:
                        status[i]=True
        return status[-1]

    def maximalSquare(self, matrix):
        # Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area., https://leetcode.com/problems/maximal-square/
        #The idea of the algorithm is to construct an auxiliary size matrix dp in which each entry dp[i][j] represents size of the square
        #sub-matrix with all 1s including matrix[i][j] where matrix[i][j] is the rightmost and bottommost entry in sub-matrix.
        #First copy first row and first columns as it is from matrix[][] to dp[][]

        if not matrix:  return 0
        m,n = len(matrix),len(matrix[0])

        dp=list(matrix)
        for i in range(m):
            dp[i][0]=int(matrix[i][0])
        for j in range(n):
            dp[0][j]=int(matrix[0][j])
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] =='1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                else:
                    dp[i][j] = 0
        ans = max([max(i) for i in dp])
        # ** is ans square
        return ans**2             


    
    def maxProfit(self, prices):
        # Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
        # for a day, either you buy or sale, if sale then max profit might be obtained if buy price is the lowest
        # mins holds lowest price until that day, if that day price is lower then the mins then update mins
        # note that you might do thing in all days (because consider all days prices are going higher), in that case K[0] is giving the answer 0
        if len(prices)==0:
            return 0
        mins=prices[0]
        K=[0 for i in range(len(prices))]
        for i in range(1,len(prices)):
            K[i]=prices[i]-mins
            if prices[i]<mins:
                mins=prices[i]
        return max(K)

    def maxProfit1(self, prices):
        # same problem above but condition: you may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
        # for a day, either you buy or sale, if sale then max profit is obtained the day you earned highest profit from buing that one one (maxBuy tack this)
                
        if not prices:  return 0
        buy=[0 for x in prices]
        sale=[0 for x in prices]

        maxBuy=-prices[0]
        maxSale=0

        for i in range(1,len(prices)):
            # if we buy today, max profit is maxSale we have achieved in a selling day minus today's buy price
            buy[i]=maxSale-prices[i]
            # maxBuy is highest buying profit upto today
            maxBuy=max(buy[i],maxBuy)
            # if we sale today maximum profit is today's price+highest profit in a previus buing day:
            sale[i]=maxBuy+prices[i]
            # maxSale is highest sale profit upto today
            maxSale=max(sale[i],maxSale)            
        return max(sale)
       
solution=Solution()
#print solution.minDistance("a","b")
#print solution.knapsack01([9,14,16,30],[2,3,4,6],10)
#print solution.knapsack01([3,7,2,9],[2,3,4,5],5)
#print solution.rob([4,1,7,12,3])
#print solution.climbStairs(4)
#print solution.minPathSum([[1,2,3],[4,5,6],[7,8,9]])
#print solution.maxProduct([1,2,-3,4,5,2,1])
#solution.maximumValueContiguousSubsequence([2,7,-10,-1,5,7,10])
#print solution.MakingChange(267,[1,5,10,50,100])
#solution.LongestIncreasingSubsequence([5,3,7,10,15,4,3])
#print solution.maxProduct([-1,-2,-9,-6])
#print solution.minimumTotal([[2],[3,4]])
#print solution.wordBreak("as",[""])
#print solution.canJump([3,2,1,0,4])
#print solution.canCompleteCircuit([15,0],[10,10])
#print solution.maximalSquare([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']])
#print solution.uniquePathsWithObstacles([[1]])
#print solution.maxProfit1([3,4,1,5,7])
#print solution.rob2([2,7,9,3,1])
#print solution.canCompleteCircuit([1,2],[2,1])
print solution.LongestIncreasingSubsequence([10,9,2,5,3,7,101,18])


