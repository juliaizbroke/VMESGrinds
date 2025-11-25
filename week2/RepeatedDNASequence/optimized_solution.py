class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashSet = set()
        answer = set()
        for i in range(len(s) -9):
            seq = s[i:(i+10)]
            if seq not in hashSet:
                hashSet.add(seq)
            else:
                answer.add(seq)
        return list(answer)