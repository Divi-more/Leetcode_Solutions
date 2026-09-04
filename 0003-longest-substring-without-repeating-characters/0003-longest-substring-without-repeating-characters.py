class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        max_len = 0 

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[i])

            length = i - left + 1
            max_len = max(max_len, length)

        return max_len