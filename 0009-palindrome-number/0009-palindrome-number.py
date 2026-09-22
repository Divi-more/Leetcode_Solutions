class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x=str(x)

        palindrome = False

        if x == x[::-1]:
            palindrome=True
        else:
            palindrome=False

        return palindrome 