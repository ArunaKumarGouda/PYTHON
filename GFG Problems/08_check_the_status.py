class Solution:
    def checkStatus(self, a, b, flag):
        # Case 1: at least one non-negative AND flag is False
        case1 = (a >= 0 or b >= 0) and not flag
        
        # Case 2: both negative AND flag is True
        case2 = (a < 0 and b < 0) and flag
        
        return case1 or case2


# Example testing
obj = Solution()
print(obj.checkStatus(5, -2, False))   # True
print(obj.checkStatus(-5, -2, True))   # True
print(obj.checkStatus(5, 2, True))     # False
