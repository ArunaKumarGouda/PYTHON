class Solution:
    def factorial(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
n = int(input("Enter a number: "))

obj = Solution()
print("The factorial of ", n, " is ", obj.factorial(n))
