def fibonacciRecursive(num):
    if num<=1:
        return num
    return fibonacciRecursive(num-1)+fibonacciRecursive(num-2)

def fibonacciDP(num):
    if num<=1:
        return num
    m=[0 for i in range(num)]
    m[1]=1
    for i in range(2,num):
        m[i]=m[i-1]+m[i-2]
    return m[num-1]

def fibonacciRecursiveMemoization(num,m): # at the beginnning all entries of m is float('inf') meaning not yet been calculated
    if num<=1:
        m[num]=num
    if m[num]!=float('inf'):
        return m[num]
    else:   # in another way we can check if m[num-1] or m[num-2] has been calcuated then add them (then second if is not required). this reduces recursive calls
        m[num]=fibonacciRecursiveMemoization(num-1,m)+fibonacciRecursiveMemoization(num-2,m)
        return m[num]
        

def subsetSum(nums,sums):
    # Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
    # a recursive solution with exponential time complexity is below. it can be implemented by DP with pseudo polynomial time complexity (sums is not polynomial in the length of the input though, which is what makes it pseudo-polynomial)

    #if more sums to cover but no numbers left then false
    if not nums and sums>0:
        return False
    #we have got the sum
    if sums==0:
        return True
    #if the last element is greater than the sum exclude it
    if nums[-1]>sums:
        return subsetSum(nums[:len(nums)-1],sums)
    #else either include or exclude the last num
    return subsetSum(nums[:len(nums)-1],sums) or subsetSum(nums[:len(nums)-1],sums-nums[len(nums)-1]) 

def partitionProblem(nums):
    #Determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.
    # others, http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
    #this problem has exponential time complexity, a DP implementation is below

    # a simiar problem: Given an array, divide it into two subsets such that the difference between the sum of subsets is minimized. Also, return the subsets.

    if not nums:
        return True

    #if sum of nums is odd then no partitioning possible
    if sum(nums)%2 ==1:
        return False
    else:
        #else if we find a subset with sum of half of the original then we are done
        return subsetSum(nums,sum(nums)/2 )

def partitionProblem(nums):
    # M(i,j) says if we have j numbers from nums can we make a sum of i from those
    if not nums:
        return True
    if sum(nums)%2 ==1:
        return False
    else:
        sums=sum(nums)/2
        M=[[False for j in range(len(nums)+1)]for i in range(sums+1)]
        for j in range(len(nums)+1):
            M[0][j]=True

        for i in range(1,sums+1):
            for j in range(1,len(nums)+1):
                #if the last element is greater than the sum exclude it
                if nums[j-1]>i:
                    M[i][j]=M[i][j-1]
                #else either include or exclude the last num
                else:
                    M[i][j]=M[i][j-1] or M[i-nums[j-1]][j-1]
    return M[sums][len(nums)]


def coinGame(coins):
    #  coins are lined up (eg. 100 200 50 2) Two players playing this game can pick a coin from either of the left or right end. Player with maximum sum will win.
    # Both players are optimally playing the game. You have to tell that whatturn(1 or 2) should be chosen in order to win. Like in above example if you play first then can select coin 2(you want to get that 200 coin to win).

    # solution: if player 1 can pick the first or last one
    # either case, other player will maximize rest of the coins, so player 1 will get minimum, so he has to pick first or last the one that is maximum 
    
    if not coins:   return 0
    if len(coins)<2:   return max(coins)
    return max(coins[0]+ min(coinGame(coins[2:]),coinGame(coins[1:len(coins)-1])), coins[len(coins)-1]+ min(coinGame(coins[1:len(coins)-1]),coinGame(coins[0:len(coins)-2])))

def coinGameDP(coins):
    m=len(coins)
    dp=[[1 for j in range(m)] for i in range(m)]
    #dp=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    for iteration in range(m):
        for i in range(0,m-iteration):
            #for j in range(i+iteration):
                #print i,i+iteration
                #print dp[i][i+iteration]
            j=i+iteration
            dp[i][j]=max(coins[i]+ min(dp[i+2][j],dp[i+1][j-1]), coins[j]+ min(dp[i+1][j-1],dp[i][j-2]))
    
    
    
if __name__=="__main__":
    #print partitionProblem([1,5,11,5])\
    #print fibonacciRecursive(4)
    #print fibonacciDP(5)
    #m=[float('inf') for i in range(5)]
    #print fibonacciRecursiveMemoization(4,m)    
    #print coinGameDP([100,200,50,2])
        

    

