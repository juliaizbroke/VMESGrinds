class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boat = 0
        while l <= r:
            remain = limit - people[r]
            r -= 1
            if remain >= people[l]:
                l +=1
            boat +=1
        return boat