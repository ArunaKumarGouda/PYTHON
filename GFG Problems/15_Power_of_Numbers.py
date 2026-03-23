

class Solution:
    def reverseExponentiation(self, n):
        r = int(str(n)[::-1])
        return n ** r
    
obj = Solution()
print(obj.reverseExponentiation(1234))   
