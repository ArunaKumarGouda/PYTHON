class Solution:
    def printTillN(self, N):
        #code here 
        def helper(n):
            if n == 0:
                return
            helper(n - 1)
            print(n, end=" ")
        helper(N)
