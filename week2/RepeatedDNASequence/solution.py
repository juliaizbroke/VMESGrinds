class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        j = 10
        hashMap = {}
        answer = []
        for i in range(len(s)):
            if i+j <= len(s):
                hashMap[s[i:(i+j)]] = hashMap.get(s[i:(i+j)], 0) +1
        for key,value in hashMap.items():
            if value > 1:
                answer.append(key)
        return answer