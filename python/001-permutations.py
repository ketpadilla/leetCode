## Problem: 46. Permutations
from itertools import permutations 

class Solution(object):
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    # * Solution 1: Using itertools
    # perm = permutations(nums)
    # return print(list(perm))
  
    # * Solution 2: Backstracking
    perm = list()
    self.backtrack(nums, perm, [])
    return print(perm)
  
  
  def backtrack(self, nums, perm, temp):
    if len(temp) == len(nums):
      perm.append(temp[:])
    else:
      for i in range(len(nums)):
        if nums[i] in temp:
          continue
        temp.append(nums[i])
        self.backtrack(nums, perm, temp)
        temp.pop()
    

# Test
if __name__ == "__main__":
    nums = [1, 2, 3]
    Solution().permute(nums)

