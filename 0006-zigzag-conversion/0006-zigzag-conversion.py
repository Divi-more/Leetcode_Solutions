class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # if only 1 row:
        if numRows == 1:
            return s

        # create rows: rows = ["", "", ""] as numRows=3
        rows = [""] * numRows
        current_row = 0
        direction = 1   # to decide whether to move or not (1=down, -1=up)

        for ch in s:
            # row 0 = p
            rows[current_row] += ch

            # current row = 2(last), -1: upward
            if current_row == numRows - 1:
                direction = -1
            # else 1: downward
            elif current_row == 0:
                direction = 1

            # 0 - down or 2 - up
            current_row += direction
        return "".join(rows)