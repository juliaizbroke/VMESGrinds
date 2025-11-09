class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Compare character by character across all strings
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                # Check if we've reached end of current string or found mismatch
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]
                
                