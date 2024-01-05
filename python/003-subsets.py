## Problem: 78. Subsets
from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # * Solution 1: Using a loop and list comprehension
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]

        # * Solution 2: Using itertools
        '''
        result = []
        n = len(nums)
        for i in range(n + 1):
            subsets = combinations(nums, i)
            result.extend([list(subset) for subset in subsets])
        
        '''
            
        return result
    
        
    
# Test
if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))
