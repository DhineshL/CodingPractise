#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_count_map = {}
        for num in nums:
            nums_count_map[num] = nums_count_map.get(num,0)+1

            if nums_count_map[num]>1:
                return True
        
        return False


# @lc code=end

