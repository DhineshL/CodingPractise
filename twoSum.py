# Solution 1 : Take a number from the array , sub from target, 
# check if the number is present in the remaining array other than the number subtracted
# Time Complexity is O(n2)

# Solution 2: Use map to create a map of value:index
# Look up the target value in the dictionary if present
# Reduces the complexity to O(n)
# But takes up Space complexity to O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map = self.create_index_map(nums)

        for index1 in range(len(nums)):
            num1 = nums[index1]
            num2 = target - num1
            if num2 in nums:
                index2 = index_map[num2]
                if index1 != index2:
                    return [index1, index_map[num2]]
                    
    def create_index_map(self, nums):
        index_map = {}
        for i in range(len(nums)):
            index_map[nums[i]] = i
        
        return index_map