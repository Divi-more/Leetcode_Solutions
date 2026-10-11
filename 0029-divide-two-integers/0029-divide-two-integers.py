class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        int_max = 2**31 - 1
        int_min = -(2**31)

        if dividend == int_min and divisor == -1:
            return int_max

        negative = (dividend < 0 ) != (divisor < 0 )

        a = abs(dividend)
        b = abs(divisor)
        que = 0

        while a >= b:
            temp = b
            multiple = 1

            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1 

            a -= temp
            que += multiple
        
        if negative:
            que = -que

        return que

    