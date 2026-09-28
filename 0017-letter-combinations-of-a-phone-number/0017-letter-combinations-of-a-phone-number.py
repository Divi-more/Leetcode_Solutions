class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        combo={
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        if not digits:
            return []

        res = [""]
        for i in digits:
            if int(i) not in combo:
                continue

            letters = combo[int(i)]
            new_res = []

            for prefix in res:
                for letter in letters:
                    new_res.append(prefix + letter)

            res = new_res
            
        return res
