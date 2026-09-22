class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 
        num = 0
        sign = 1
        n = len(s)
        
        while i < n and s[i] == " ":
            i += 1 

        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1

        # Apply sign
        num = num * sign

        # 4. Check 32-bit integer range
        if num < -(2**31):
            return -(2**31)

        if num > (2**31 - 1):
            return 2**31 - 1

        return num