class Solution:
    def majorityElement(self, arr):
        #code here
        n = len(arr)
        count_map = {}
        
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1
            if count_map[num] > n // 2:
                return num
                
        return -1
