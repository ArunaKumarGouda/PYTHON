class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        
        # Convert string to list (since strings are immutable in Python)
        s = list(s)
        
        while s != ['1']:
            # If even (last bit is '0')
            if s[-1] == '0':
                s.pop()  # divide by 2
            
            else:
                # Add 1 to binary string
                i = len(s) - 1
                
                # Handle carry
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                
                if i >= 0:
                    s[i] = '1'
                else:
                    s.insert(0, '1')  # if all bits were '1'
            
            steps += 1
        
        return steps

# 🔹 Taking input from user
binary_input = input("Enter binary number: ")

# 🔹 Creating object
obj = Solution()

# 🔹 Calling function
result = obj.numSteps(binary_input)

# 🔹 Printing result
print("Number of steps:", result)
