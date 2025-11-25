class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        # total_len = word_len * len(words)

        target = {}
        for w in words:
            target[w] = target.get(w, 0) + 1

        result = []

        for i in range(word_len):
            left = i
            right = i
            seen = {}
            count = 0

            while right + word_len <= len(s):
                w = s[right: right + word_len]
                right += word_len

                if w in target:
                    seen[w] = seen.get(w, 0) + 1
                    count += 1

                    while seen[w] > target[w]:
                        left_w = s[left: left + word_len]
                        left += word_len
                        seen[left_w] -= 1
                        count -= 1

                    if count == len(words):
                        result.append(left)

                else:
                    seen.clear()
                    count = 0
                    left = right

        return result
