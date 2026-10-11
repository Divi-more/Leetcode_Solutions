class Solution(object):
    def findSubstring(self, s, words):
        from collections import Counter
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        word_count = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]

                if word not in word_count:
                    seen.clear()
                    count = 0
                    left = right + word_len
                    continue

                seen[word] += 1
                count += 1

                while seen[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len
                
                if count == total_words:
                    result.append(left)

                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len
        return result