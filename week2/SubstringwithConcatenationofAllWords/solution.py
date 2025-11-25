class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)

        target = {}
        for w in words:
            target[w] = target.get(w, 0) + 1

        result = []

        for i in range(len(s) - total_len + 1):
            seen = {}

            for j in range(0, total_len, word_len):
                word = s[i + j: i + j + word_len]
                seen[word] = seen.get(word, 0) + 1

            if seen == target:
                result.append(i)

        return result
