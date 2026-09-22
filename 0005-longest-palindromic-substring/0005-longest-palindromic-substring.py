class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        longest = ""
        
        for i in range(len(s)):
            
            # Odd length palindrome
            # start from same point i.e., center (bab: a)
            left, right = i, i

            # left:pointer should not go ouside str, right:pointer should not go ouside str
            # s[left] == s[right]: check on both sides (bab: b == b)
            while left >= 0 and right < len(s) and s[left] == s[right]:

                """
                compare:
                Current palindrome length : len(s[left:right + 1])
                Previously stored longest palindrome length : len(longest)
                """
                if  len(s[left:right + 1]) > len(longest):

                    # update longest to new substring
                    longest = s[left:right + 1]
                
                # move pointers to left and right to check if theres more to palindrome str
                left -= 1
                right += 1

            # Even length palindrome
            # (abba: bb-center)
            left, right = i, i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right + 1]) > len(longest):
                    longest = s[left:right + 1]
                
                left -= 1
                right += 1
        return longest