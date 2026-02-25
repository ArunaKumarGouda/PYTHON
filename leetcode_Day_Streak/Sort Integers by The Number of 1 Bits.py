class Solution(object):
    def sortByBits(self, arr):
        def countBits(x):
            binary = bin(x).count('1')
            return (binary, x)
        
        return sorted(arr, key = countBits)

arr = list(map(int, input("Enter your numbers: ").replace(",", "").split()))

obj = Solution()
print(obj.sortByBits(arr))
