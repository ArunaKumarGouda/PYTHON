class Solution:
    def reverseexponentiation(self, n):
        # code here
        reverse_n = int(str(n)[::-1])
        
        result = n ** reverse_n
        
        return result
