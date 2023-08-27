# Solution 1 - solves by converting int to string 
# and checking for palindrome 
# time complexity O(n) & space complexity O(1)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        left = 0
        x=str(x)
        right = len(str(x)) - 1

        while left< right:
            if x[left] != x[right]:
                return False
            left+=1
            right-=1
            
        return True

        
# @lc code=end

