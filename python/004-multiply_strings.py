## Problem 43. Multiply Strings
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
    
        return str(int(num1)*int(num2))
    

# Test
if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    print(Solution().multiply(num1, num2))