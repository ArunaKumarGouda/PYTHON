#User function Template for python3

class Solution:
    def factorial (self, n):
        # code herem
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)
