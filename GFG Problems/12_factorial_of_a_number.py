class Solution:
    def factorial(self, n):
        ans = 1
        for i in range(2, n + 1):
            ans *= i
        return ans
    
n = int(input("Enter a number:"))

obj = Solution()
result = obj.factorial(n)

print(f"The factorial of {n} is {result}")
