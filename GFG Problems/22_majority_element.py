class Solution:
    def majorityElement(self, arr):
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        for key in freq:
            if freq[key] > len(arr) // 2:
                return key
        
        return -1


n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter elements: ").split()))

obj = Solution()
print(obj.majorityElement(arr))
