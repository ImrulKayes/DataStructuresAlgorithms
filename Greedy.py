class Solution:    def canJump1(self, nums):        # exceeds time limit        # at j'th index, it is reachable if any of pevious index is reachable and from a jump reaches here        # the following is a greedy solution O(n)         if len(nums)==0:            return True        M=[False for i in range(len(nums))]        M[0]=True        for i in range(1,len(nums)):            for j in range(0,i):                if M[j] and nums[j]+j>=i:                    M[i]=True        return M[-1]        def canJump(self, A):        # gready solution. At each index, calculate what max we can jump. Consider [3,2,1,0,4] at value 0, no steps are left to go anywhere        # we we could go last index then return True        # in greedy approch we are thining at an index we can reach from the step where we have max jumps, but in DP we consider all possible index where we have any possibity to jump        if not A:            return False        maxjump=0        for i in range(len(A)):            maxjump=max(maxjump-1,A[i])            if maxjump==0:                break                   return i==len(A)-1    def maximalSquare(self, matrix):        # Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area., https://leetcode.com/problems/maximal-square/        #The idea of the algorithm is to construct an auxiliary size matrix dp in which each entry dp[i][j] represents size of the square        #sub-matrix with all 1s including matrix[i][j] where matrix[i][j] is the rightmost and bottommost entry in sub-matrix.        #First copy first row and first columns as it is from matrix[][] to dp[][]        if not matrix:  return 0        m,n = len(matrix),len(matrix[0])        dp=list(matrix)        for i in range(m):            dp[i][0]=int(matrix[i][0])        for j in range(n):            dp[0][j]=int(matrix[0][j])        for i in xrange(1,m):            for j in xrange(1,n):                if matrix[i][j] =='1':                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1                else:                    dp[i][j] = 0        ans = max([max(i) for i in dp])        # ** is ans square        return ans**2                 def canCompleteCircuit1(self, gas, cost):        # we are starting from each gas station and checking whether we can return here        # this is a brtue force solution with O(n*n) complexity. A linear time solution is below        if  len(gas)<=1:            if cost[0]<=gas[0]:                return True            else:                return -1        for i in range(len(gas)):            flag=True            maxgas=gas[0]            if cost[0]>maxgas:                flag=False            else:                for j in range(1,len(gas)):                    maxgas=maxgas-cost[j-1]+gas[j]                    if maxgas<cost[i]:                        flag=False                        break            gas.append(gas.pop(0))            cost.append(cost.pop(0))            if flag:                return i        #last=len(gas)-1        return -1    def canCompleteCircuit(self, gas, cost):        #http://www.programcreek.com/2014/03/leetcode-gas-station-java/        #To solve this problem, we need to understand and use the following 2 facts:        #1) if the sum of gas >= the sum of cost, then the circle can be completed.        #2) if A can not reach C in a the sequence of A-->B-->C, then B can not make it either.        # The idea is: consider the case that, if started at station i, and when goes to the station j, there is not enough gas to go the j+1 station.        #What happened now? For the brutal force method, we go back to the sataion i+1 and do the same thing. But, actually, if the accumutive gas cannot make it from j to j+1,        # then the stations from i to j are all not the start station. That is because, (1)the tank is unlimited, every time arrive to the station, the tank will fuel the max gas here,        # and comsume the cost to go to the next. (2)There can not be negative tank when arriving a station, at least the tank is empty. So, if i to j cannot go to j+1, then i+1 to j still cannot go        #to j+1... In this way, the next starting station we will try is not i+1, but the j+1. And after a single loop from i to j, we can find the result!        sumRemaining=0 #track current remaining        total=0 #track total remaining        start=0        for i in range(0,len(gas)):            remaining=gas[i]-cost[i]            # if sum remaining of (i-1) >= 0, continue              if sumRemaining>=0:                sumRemaining+=remaining            #otherwise, reset start index to be current            else:                sumRemaining=remaining                start=i            total+=remaining        if total>=0:            return start        else:            return -1    solution=Solution()#print solution.canJump([3,2,1,0,4])#print solution.canCompleteCircuit([15,0],[10,10])#print solution.canCompleteCircuit([1,2],[2,1])