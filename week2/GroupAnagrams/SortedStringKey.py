from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())