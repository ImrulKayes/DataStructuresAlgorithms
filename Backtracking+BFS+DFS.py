class Solution:    # When face the "return all", "get all ", "find all possible", "find the total number of", an idea is to use the recursion    # 1. find all the palindromes in substring s[0], and all the palindromes in substring s[1:]    # 2. find all the palindromes in substring s[0:1], and all the palindromes in substring s[2:]    # find all the palindromes in substring s[1:len(s)], and all the palindromes in substring s[len(s):]    def partition(self, s):        if not s:            return []        return self.findPartition(s)    def findPartition(self, s):        if not s:            return [[]]        output=[]        # if s[:i] is palindrome, it will get at least one output partition from s[:i]  (as each char is palindrome)        # output is never empty from a findPartition call is s has something        for i in range(1, len(s) + 1):            if self.isPalindrome(s[:i]):                temp=[]                temp.append(s[:i])                # we expect that listlists will be a list of lists of all possbile parlindromes in s[i:]                # so we just new to add s[:i] to each of them and return                listlists=self.findPartition(s[i:])                for element in listlists:                    newtemp=temp+element                    output.append(newtemp)        return output    def isPalindrome(self, string):        low,high=0,len(string)-1        while low<=high:            if string[low]!=string[high]:                return False            low+=1            high-=1        return True        # or simply we can use--> return string == string[::-1]#solution=Solution()#print solution.partition("cdd")class Solution:    # in the following output is containing the results    # temp is containing output of each single successful iteration of s[i:] and s[:i]    # temp is a output from s[i:]  that we are passing to next iteration, so that output from s[:i] could be appended to temp and also appended to output    def partition(self, s):        if not s:            return []        output = []        self.findPartition(s, output, [])        return output    def findPartition(self, s, output, temp):        if not s:            output.append(temp[:])            return        for i in range(1, len(s) + 1):            if self.isPalindrome(s[:i]):                temp.append(s[:i])                print temp,'---'                self.findPartition(s[i:], output, temp)                # we are popping beacuse output related to s[:i] has been got and appended to output                temp.pop()                print temp    def isPalindrome(self, string):        return string == string[::-1]#solution=Solution()#print solution.partition("bb")class Solution:    # we have 123 and we want to take two, take 1 fixed then get 1 from remaning 23+ take 2 fixed and get one from remaining 3    # good backtracking solution is below        def combine(self, n, k):        if n==0 or k>n:            return []        nums=range(1,n+1)        dic={}        output=self.combine1(nums,k)                                       for x in output:            x=sorted(x)            dic[str(x)]=x        output=[]        for k,v in dic.iteritems():            output.append(v)         return output    def combine1(self, nums, k):        if k==0:            return [[]]        output=[]        for i in range(len(nums)):            lists=self.combine1(nums[i+1:],k-1)            for element in lists:                element.append(nums[i])                output.append(element)        return output#solution=Solution()#print solution.combine(4,2)class Solution:    # good backtracking solution is below    # Applying the same concept from combination, but exceeds time limit :(    # them problem here is that if two elements sum is bigger than target there is no point to check whether three element that includes those two    # but there is no control of that here, an alternate solution is betlow    def combinationSum22(self, candidates, target):        if len(candidates)==0:            return []        dic={}        m=len(candidates)+1        output=[]        for k in range(1,m):            output+=self.combinationSum21(candidates,target,k)        #print output        for x in output:            x=sorted(x)            if sum(x)==target:                dic[str(x)]=x        output=[]        for k,v in dic.iteritems():            output.append(v)         return output    def combinationSum21(self, nums, target,k):        if k==0:            return [[]]        output=[]        for i in range(len(nums)):            if nums[i]<target:                lists=self.combinationSum21(nums[i+1:],target,k-1)                for element in lists:                    element.append(nums[i])                    #print sum(element)                    #if sum(element)==target:                    output.append(element)        return outputclass Solution:    # good backtracking solution is below       def combinationSum2(self, candidates, target):        ans=[]        candidates.sort()        for ii,elem in enumerate(candidates):            # if the element is less than target then find all other combinations from remaining numbers that have sum target-element            # and add the element to them            if target>elem:                subList=self.combinationSum2(candidates[ii+1:],target-elem)                if subList:                    # add the element to all the results lists                     ans+=[[elem]+lis for lis in subList if [elem]+lis not in ans]            elif target==elem:                if [elem] not in ans:                    ans+=[[elem]]            # if the element is greater than target then there is no point to continue on remaining numbers as they are higher than the target             else:                break        return ans    def subsets(self, nums):        # e.g., 123, for 1 we will get [],1,12,123,13 for 2 we gill get 2,23, and for 3 we will get 3, combination of these are the result        # we do backtracking using line and storing results to res        nums.sort()        res=[]        line=[]        self.subsetsHelper(nums,res,line)        return res    def subsetsHelper(self,nums,res,line):        res.append(line)        for i,x in enumerate(nums):            self.subsetsHelper(nums[i+1:],res,line+[x])    def permute(self, nums):        # e.g., 123 keep 1 fix and get permutation of 23 (2,3 and 3,2), so we are getting 123,132        # do the same for other digits also        res=[]        # results        line=[]        # backtracker, holds running output, will copy content to results once reach a single permutation result e.g., 132, must pop after calling           self.permuteHelper(nums,res,line)        return res    def permuteHelper(self,nums,res,line):        # when no other num left copy the result to res        if not nums:            res.append(line[:])        for i,x in enumerate(nums):            line.append(x)               # do recursion with remaining numbers            self.permuteHelper(nums[:i]+nums[i+1:],res,line)  # or we can do res+[x] to avoid line.append(x)  and line.pop()            line.pop()    def permuteUnique(self, nums):        # using the same technique, ony exception we will not proceed with a number if we find it previous (becasue in that case all permutations start with the number has been done)        res=[]        line=[]        self.permuteUniquehelper(nums,res,line)        return res    def permuteUniquehelper(self,nums,res,line):        # when no other num left copy the result to res        if not nums:            res.append(line[:])        for i,x in enumerate(nums):            if x not in nums[:i]:                line.append(x)                # do recursion with remaining numbers                self.permuteUniquehelper(nums[:i]+nums[i+1:],res,line)                line.pop()    def combine(self, n,k):        # e.g., n=1234 keep 1 fix and get combination of 234 for k=1, result: 12,13,14 then keep 2 fix and get combination of 34 for k=1, result:23,24.....finally combine all results        # do the same for other digits also        res=[]        # results        line=[]        # backtracker, holds running output, will copy content to results once reach a single combination result e.g., 13, must pop after calling           # we need to use k also backtracker as well as line as k will decide whether we will go more deeply        self.combineHelper([x for x in range(1,n+1)],res,line,k)        return res    def combineHelper(self,nums,res,line,k):        # when k==0 then copy results from line to res        if k==0:            res.append(line)        for i,x in enumerate(nums):            k-=1            # do recursion with remaining numbers            self.combineHelper(nums[i+1:],res+[x],line,k)            k+=1    def combinationSum(self, candidates, target):            res=[]        # results        line=[]        # backtracker, holds output        self.combinationSumHelper(sorted(candidates),res,line,target)        return res    def combinationSumHelper(self,nums,res,line,target):        if target==0:            res.append(line[:])            return        for i,x in enumerate(nums):            if x<=target:                line.append(x)                self.combinationSumHelper(nums[i:],res,line,target-x)                line.pop()#solution=Solution()#print solution.combinationSum2([10,1,2,7,6,5,1],8)class Solution:    def combinationSum(self, candidates, target):        ans=[]        candidates.sort()        for ii,elem in enumerate(candidates):            # if the element is less than target then find all other combinations from remaining numbers that have sum target-element and also do it again to the current combination but now targer is target-elemet            # as we dont mind repeating one element            # and add the element to them            if target>elem:                subList1=self.combinationSum(candidates[ii:],target-elem)                subList2=self.combinationSum(candidates[ii+1:],target-elem)                if subList1:                    # add the element to all the results lists                     ans+=[[elem]+lis for lis in subList1 if [elem]+lis not in ans]                if subList2:                    # add the element to all the results lists                     ans+=[[elem]+lis for lis in subList2 if [elem]+lis not in ans]            elif target==elem:                if [elem] not in ans:                    ans+=[[elem]]            # if the element is greater than target then there is no point to continue on remaining numbers as they are higher than the target             else:                break        return ans#solution=Solution()#print solution.combinationSum([2,3,6,7],7)class Solution:    # same techniqe as combinationSum, but limiting number of digits    def combinationSum3(self, k, n):        return self.combinationSum(range(1,10),k,n)            def combinationSum(self, candidates,k,target):        ans=[]        candidates.sort()        for ii,elem in enumerate(candidates):            # if the element is less than target then find all other combinations from remaining numbers that have sum target-element and also do it again to the current combination but now targer is target-elemet            # as we dont mind repeating one element            # and add the element to them            if target>elem:                if k>0:                    subList=self.combinationSum(candidates[ii+1:],k-1,target-elem)                    if subList:                    # add the element to all the results lists                         ans+=[[elem]+lis for lis in subList if [elem]+lis not in ans]                else:                    return ans            elif target==elem:                #print target,k                if k==1:                    if [elem] not in ans:                        ans+=[[elem]]                else:                    return ans            # if the element is greater than target then there is no point to continue on remaining numbers as they are higher than the target             else:                break        return ans    def ladderLength(self, beginWord, endWord, wordDict):        # we will use backtracking to compare all solutons and return the shortest lenghth        # from beginWord, we will get all words that are in the wordDict and has difference 1        # from each of them we will do this recursively         # otherwise, this is a search problem, BFS (bi directional) can also give optimal solution, then the shortest path is also not a problem        x=self.ladderLength1(beginWord, endWord, wordDict,1)        return x     def ladderLength1(self, beginWord, endWord, wordDict,k):                distOne=self.listDistOne(beginWord,wordDict)        if not wordDict or not distOne:            return 0        if len(self.listDistOne(beginWord,[endWord]))==1:            print k+1,beginWord            return k+1        mins=10000        print beginWord,distOne,k        for i in range(len(distOne)):            if len(self.listDistOne(distOne[i],[endWord]))==1:                k1=k+1            else:                k1=self.ladderLength1(wordDict[i],endWord,wordDict[:i]+wordDict[i+1:],k+1)            if k1<mins:                mins=k1        return mins                  def listDistOne(self,beginWord,wordDict):        output=[]        for x in wordDict:            count=0            for i in range(len(x)):                if x[i]!=beginWord[i]:                    count+=1            if count==1:                output.append(x)        return output    def exist(self, board, word):        # using backtracking we go through all possible solutions starting from each chars of the 2D grid        # convert the original string board to list board, beacuse string is difficult to mutate in python        m,n=len(board),len(board[0][0])        board1=[[1 for j in range(n)] for i in range(m)]        for i in range(m):            for j in range(n):                board1[i][j]=board[i][0][j]        result = False            # for each char check the word could be possible starting from that        for i in range(m):            for j in range(n):                if self.dfs(board1,word,i,j,0):                    return True        return result     def dfs(self,board,word,i,j,k):        m,n=len(board),len(board[0])        if i<0 or j<0 or i>=m or j>=n:            return False        # if current board char matches the expected char then seach left unmatched chars, starting a new dfs        # make the matched char in the board flagged by # (we don't want to traverse it again for rest of the solution)        # however, return true if all chars in the word have been matched        if board[i][j]==word[k]:            temp=board[i][j]            board[i][j]='#'            if k==len(word)-1:                return True            else:                if self.dfs(board,word,i-1,j,k+1) or self.dfs(board,word,i+1,j,k+1) or self.dfs(board,word,i,j-1,k+1) or self.dfs(board,word,i,j+1,k+1):                    return True            # we have to keep the original board ( because of call be reference is happening)            board[i][j]==temp        return False    def grayCode(self, n):         if n==0: return [0]        return self.back(n)     def back(self, n):        # based on obervation        # n = 0, [0]        # n = 1, [0, 1]        # n = 2, [0, 1, 3, 2]        # n = 3, [0, 1, 3, 2, 6, 4, 7, 5]        # each time just append the original list with the revesed list and add 2 ** (n-1)        if n==1:            return [0,1]         cur = []         pre= self.back(n-1)        for x in xrange(len(pre)-1,-1,-1):            cur.append(2**(n-1)+pre[x])          return pre+cur     def generateParenthesis(self, n):        # will try to generate all possible combinations and will backtrack if condistions breaks        # l and r represents the remaining number of ( and ) that need to be added.         # When l > r, there are more ")" placed than "(". Such cases are wrong and the method stops.        res=[]        st=[]        self.generateParenthesis1(res,st,n,n)        return res    def generateParenthesis1(self,res,st,l,r):        # if we have a (, then we can only add a ), otherwise not possible, l, r tracks this, they indicate how many braces left        if l>r: return        if l==0 and r==0:            res.append(''.join(st))            return         # if you use  + in in backtracker, no need to pop        if l>0:            self.generateParenthesis1(res,st+["("],l-1,r)        if r>0:            self.generateParenthesis1(res,st+[")"],l,r-1)      def dis(self,node,st):        count=0        for i in range(len(node)):            if node[i]!=st[i]:                count+=1                if count>1:                    return False        return True    def ladderLength(self,strs,source,target):        #Given list of dictionary words. Find minimum number of trials to reach from source word to destination word where word traversal is allowed through 1 letter difference.        #make a graph where nodes are connected if they have 1 char difference, then BFS and shortest path        graph={}        for i in range(len(strs)):            node=strs[i]            for st in strs[:i]+strs[i+1:]:                if self.dis(node,st):                    graph.setdefault(node,[]).append(st)        thisLabel=[source]        if not graph or not graph.has_key(source):            return 0        visited={}        count=1        while thisLabel:            nextLabel=[]            for node in thisLabel:                visited[node]=1                for neighbor in graph[node]:                    if neighbor==target:                        return count+1                    if not visited.has_key(neighbor):                        nextLabel.append(neighbor)            count+=1            thisLabel=nextLabel                    return 0    def numIslands(self, grid):        # Given a 2d grid map of 1's (land) and '0's (water) count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.        # (You may assume all four edges of the grid are all surrounded by water.)                # island is connected vertically and horizontally 1s with four sides 0s        # for each grid if we get 1 then will count++ and make all adjacent 1's (four) 0, recursively        # this solution could be thought as a BFS        # if no grid or one row or one column  then no island        if not grid or len(grid)==0 or len(grid[0])==0:            return 0                m,n=len(grid),len(grid[0])        count=0        for i in range(m):            for j in range(n):                if grid[i][j]:                    count+=1                    self.margeGrid(grid,i,j)        return count    def margeGrid(self,grid,i,j):        m,n=len(grid),len(grid[0])        if i<0 or j<0 or i>=m or j>=n:            return        if grid[i][j]==0:            return                #this element was 1, so make it 0 (visited)        grid[i][j]=0        self.margeGrid(grid,i+1,j)        self.margeGrid(grid,i-1,j)        self.margeGrid(grid,i,j+1)                self.margeGrid(grid,i,j-1)     def solve(self, board):        # Given a 2D board containing X and 0, capture regions surrounded by X, A region is captured by flipping all 0s into Xs in that surrounded region.        # https://leetcode.com/problems/surrounded-regions/                # this solution is based on numIslands        # if an element is 0 then recusively check all four adjacent elements, if they are not X then 0 should remain 0, otherwise make it X        # another easy solution is here https://leetcode.com/discuss/42445/a-really-simple-and-readable-c-solution%EF%BC%8Conly-cost-12ms        # First, check the four border of the matrix. If there is a element is 'O', alter it and all its neighbor 'O' elements to '1'.        # Then ,alter all the 'O' to 'X'        # At last,alter all the '1' to 'O'        if not board or len(board)==0 or len(board[0])==0:            return        m,n=len(board),len(board[0])        count=0        for i in range(1,m-1):            for j in range(1,n-1):                if board[i][j]=='0':                    x=self.margeBoard(board,i,j)                            print board    def margeBoard(self,board,i,j):        m,n=len(board),len(board[0])        #only a boundary element is 0 then it will remain 0 and all neightbours of it will remain 0 (so returning false)         if i==0 or j==0 or i==m-1 or j==n-1:            if board[i][j]=='0':                return False        # make the 0 element X, we will later change it if all four negighbours are not 0        board[i][j]='X'        # if all four neighbors are X then return True        if board[i+1][j]=='X' and board[i-1][j]=='X' and board[i][j+1]=='X' and board[i][j-1]=='X':            return True        # recrusively check the neighbors         a=b=c=d=True        if board[i+1][j]=='0':            a=self.margeBoard(board,i+1,j)        if board[i-1][j]=='0':            b=self.margeBoard(board,i-1,j)        if board[i][j+1]=='0':            c=self.margeBoard(board,i,j+1)                    if board[i][j-1]=='0':            d=self.margeBoard(board,i,j-1)         if a and b and c and d:            return        else:            # if any of the neighbors is not X then this element should remain 0            board[i][j]=='0'            return        solution=Solution()#print solution.combinationSum3(3,9)#solution.ladderLength("hit","cog",["hot","dot","dog","lot","log"])#print solution.exist([["ABCE"],["SFCS"],["ADEE"]],"ABCCD")#print solution.exist(["aa","cd"],"acbd")#solution.numIslands([])#solution.numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])#solution.solve([['X','X','X','X'],['X','0','0','X'],['X','X','0','X'],['X','0','X','X']])#solution.solve([['X','X','X'],['X','0','X'],['X','X','X']])print solution.ladderLength(['ABC','ACD','BBC','BCC','BCD','BDC','ABD','BDE','AGF'],"ABC","BCC")