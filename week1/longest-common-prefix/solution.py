class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        
        for word in strs:
            for j in range(len(shortest)):
                if word[j] == shortest[j]:
                    continue
                else:
                    shortest = word[:j]
                    break
        return shortest
        