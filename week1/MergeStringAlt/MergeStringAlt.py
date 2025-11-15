class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = len(word1)
        j = len(word2)
        long_word = i if i>j else j
        result = ''
        for k in range (long_word):
            if (i>0): 
                result += word1[k]
            else: 
                result += word2[k:]
                break

            if (j>0):
                result += word2[k]
            else:
                result += word1[k+1:]
                break
            i -= 1
            j -= 1

        return result
    
# Example usage:
solution = Solution()
print(solution.mergeAlternately("abcdef", "pqr"))  # Output: "apb