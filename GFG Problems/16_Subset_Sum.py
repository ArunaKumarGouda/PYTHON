class Solution:
    def subsetSum(self, arr):

        result = []

        def dfs(i, current_sum):
            if i == len(arr):
                result.append(current_sum)
                return

            dfs(i+1, current_sum + arr[i])  # include
            dfs(i+1, current_sum)           # exclude

        dfs(0, 0)
        return result


arr = list(map(int, input("Enter numbers separated by space: ").split()))

obj = Solution()
print(obj.subsetSum(arr))
