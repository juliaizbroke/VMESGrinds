import math

class Solution:
    def pickGifts(self, gifts, k: int) -> int:
        for i in range(k):
            largest = max(gifts)
            gifts.remove(largest)
            gifts.append(int(math.isqrt(largest)))
        return sum(gifts)