class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = {}
        s = s.split()
        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashMap:
                if s[i] in hashMap.values():
                    return False
                hashMap[pattern[i]] = s[i]
        
        for index, value in enumerate(pattern):
            if hashMap[value] != s[index]:
                return False
        return True