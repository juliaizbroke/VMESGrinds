class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = {}
        subStr = ''
        long = 0
        if len(s) < 2:
            return len(s)
        for i in range(len(s)):
            subStr = subStr + s[i]
            if s[i] in track and s[i] in subStr[:-1]:
                subStr = s[track[s[i]]+1:i+1]
            track[s[i]] = i
            if long < len(subStr):
                long = len(subStr)
        return long

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))