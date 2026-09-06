class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # check if num is +ve or -ve
        sign = -1 if x < 0 else 1
        # convert to absolute value i.e., +ve
        x = abs(x) 

        rev = 0

        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10 # 123 // 10 = 12

        rev *= sign

        if rev < -(2**31) or rev > (2**31 - 1):
            return 0 

        return rev