#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str_len1 = len(s)
        str_len2 = len(t)
        TOTAL_ALPHABET_COUNT = 26
        LOWER_ASCII_START_COUNT = 97
        if str_len1 != str_len2:
            return False
        
        word_count = []

        for i in range(TOTAL_ALPHABET_COUNT):
            word_count.append(0)
    
        for i in range(str_len1):
            word_count[ord(s[i])-LOWER_ASCII_START_COUNT] += 1
            word_count[ord(t[i])-LOWER_ASCII_START_COUNT] -= 1
        
        for k in range(TOTAL_ALPHABET_COUNT):
            if word_count[k] != 0:
                return False

        return True


        
# @lc code=end

