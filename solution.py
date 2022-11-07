#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        d=dict()
        k=0
        for val in arr:
            if val not in d:
                d[val]=1
            else:
                d[val]+=1
        for val in arr:
            if d[val]<2:
                return val
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends
