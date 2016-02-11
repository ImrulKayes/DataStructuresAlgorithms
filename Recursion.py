'Given a stack, sort it using recursion. Use of any loop constructs like while, for..etc is not allowed.''http://www.geeksforgeeks.org/sort-a-stack-using-recursion/'def sortStack(stack):    'for the top assume that all remaining stack is sorted and insert the top in appropriate position using insertStack'    if not stack:        return    top=stack.pop()    sortStack(stack)    insertStack(stack,top)def insertStack(stack,top):    if not stack:        stack.append(top)        return    'if top is greater than the currentTop then insert here'    if stack[-1]<=top:        stack.append(top)    else:        'else recurse to find an appropriate position, remember to add the current top after returning'        currTop=stack.pop()        insertStack(stack,top)        stack.append(currTop)'driver function'if __name__=="__main__":    stack=[-3,14,18,-5,30]    sortStack(stack)    print stack'Print all non-increasing sequences of sum equal to a given number x''x=3 output=[[1, 1, 1], [2, 1], [3]]''for 3, output= 3+(0), 2+(1),1+(2), we are keeping numPrev to keep the parent so that non-increasing sequences are maintained e.g., 1+(2)--> for 2 we can only call with 1, not 2'def nonIncSeq(num):    return nonIncSeqUtil(num,num)def nonIncSeqUtil(num,numPrev):    if num==0:        return None    if num==1:        return [[1]]    res=[]    for i in range(1,num+1):        if i<=numPrev:            temp=nonIncSeqUtil(num-i,i)            if not temp:                res.append([i])            else:                for alist in temp:                    alist.insert(0,i)                res+=temp    return resif __name__=="__main__":    print nonIncSeq(4)"Print a pattern without using any loop"Input: n = 10"Output: 10, 5, 0, 5, 10"def printSeq(num):    print num    if num<=0:        return    printSeq(num-5)    print num        'Given a string, print all possible palindromic partitions'#'e.g., "nitin"=[['n', 'i', 't', 'i', 'n'], ['n', 'iti', 'n'], ['nitin']]'def palindromePartition(strs):    'if nitin, for first n, if n is palindrome then n+ paindromes from reminined strs is the answer'    if not strs:        return [[]]    res=[]    for i in range(len(strs)):        if isPalindrome(strs,i):            temp=palindromePartition(strs[i+1:])            for alist in temp:                res.append([strs[:i+1]]+alist)    return res                def palindromePartitionWithMeoization(strs,m):    'same previous approach but memoization of recursions'    if not strs:        return [[]]    res=[]    for i in range(len(strs)):        if isPalindrome(strs,i):            if m.has_key(strs[i+1:]):                temp=m[strs[i+1:]]            else:                temp=palindromePartitionWithMeoization(strs[i+1:],m)                m[strs[i+1:]]=temp            for alist in temp:                res.append([strs[:i+1]]+alist)    return resdef isPalindrome(strs,i):    mid=(i+1)/2    for j in range(mid):        if strs[j]!=strs[i-j]:            return False    return Trueif __name__=="__main__":    strs="nitin"    print palindromePartitionWithMeoization(strs,{})    print palindromePartition(strs)'Minimum steps to reach a destination http://www.geeksforgeeks.org/minimum-steps-to-reach-a-destination/''You can go left or right starting from 0, but at step i you have to take i steps'def minSteps(target):    return minStepUtil(0,1,target)def minStepUtil(curr,jumpSize,target):    if abs(curr)>abs(target):   return float('inf')    if curr==target:        return 0    right=minStepUtil(curr+jumpSize,jumpSize+1,target)    left=minStepUtil(curr-jumpSize,jumpSize+1,target)    return min(left,right)+1if __name__=="__main__":    print minSteps(11)'Given two sorted arrays A and B, generate all possible arrays such that first element is taken from A then from B then from A and so on in increasing order till the arrays exhausted.'The generated arrays should end with an element from B. http://www.geeksforgeeks.org/generate-all-possible-sorted-arrays-from-alternate-elements-of-two-given-arrays/'def sortedArrays(A,B):    if not A or not B:        return [[]]    res=[]    for i in range(len(A)):        for j in range(len(B)):            'compare pair of A and B, if A is smaller then result is this pair and recursive result from rest of the A and B'            if A[i]<=B[j]:                res.append([A[i],B[j]])                temp=sortedArrays(A[i+1:],B[j+1:])                for alist in temp:                    'for rest of the result we are only considering increasing orders'                    if alist:                        if B[j]<=alist[0]:                            res.append([A[i],B[j]]+alist)    return resif __name__=="__main__":    print sortedArrays([10,15,25],[1,5,20,30])    #print sortedArrays([10],[20,30])'Print all increasing sequences of length k from first n natural numbers. http://www.geeksforgeeks.org/print-increasing-sequences-length-k-first-n-natural-numbers/''k=2 and n=3, res=[[1, 2], [1, 3], [2, 3]]. Use simple backtracking'def incSecK(k,n):    res=[]    incSecUtil(k,n,[],res)    print resdef incSecUtil(k,n,temp,res):    if k==0:        res.append(temp)        return    for i in range(1,n+1):        'when no temp, consider all branches'        if not temp:           incSecUtil(k-1,n,temp+[i],res)        else:            'only considering the braches that are higher than last number'            if i>temp[-1]:                incSecUtil(k-1,n,temp+[i],res)if __name__=="__main__":    print incSecK(3,5)'https://github.com/rohitsinha54/ArrayHopper'import sysdef arrayHopper(nums):    next={}    cache={}    arrayHopperUtil(0,nums,next,cache)    if not next:        print 'failure'        return    start=0    st=[]    while next[start]:        st.append(str(start))        start=next[start]    st.append('out')    print ','.join(st)    def arrayHopperUtil(curr,nums,next,cache):    if curr>=len(nums):        next[curr]=None        return 0    if nums[curr]==0:        return -1    min=float('inf')    for i in range(1,nums[curr]+1):        if cache.has_key(curr+i):            hops=cache[curr+i]        else:            hops=arrayHopperUtil(curr+i,nums,next,cache)            cache[curr+i]=hops        if hops!=-1:            if hops<=min:                min=hops                next[curr]=curr+i    return min+1 if min!=float('inf') else -1        if __name__=="__main__":    nums=[]    #for line in open(str(sys.argv[1])):    #    nums.append(int(line.strip()))    #arrayHopper(nums)    #arrayHopper([5,6,0,4,2,4,1,0,0,4])        nums=[]    if len(nums)>=1:        arrayHopper(nums)    else:        print 'failure'     