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
        if str_len1 != str_len2:
            return False
        
        word_map = {}
    
        for i in range(str_len1):
            word_map[s[i]] = word_map.get(s[i],0) + 1
            word_map[t[i]] = word_map.get(t[i],0) - 1
        
        for k in word_map.keys():
            if word_map[k] != 0:
                return False
        
        return True


        
# @lc code=end

