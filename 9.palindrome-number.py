# Solution 1 - solves by converting int to string 
# and checking for palindrome 
# time complexity O(n) & space complexity O(1)
# Solution 2 - reverse the number & check if both the number are same

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_x=0
        num = x
        while num >0:
            reminder = num%10
            num //= 10
            rev_x*=10
            rev_x+=reminder

        if rev_x==x:
            return True
        else:
            return False


