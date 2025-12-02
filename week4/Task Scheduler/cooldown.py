import heapq


def leastInterval(tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        tasks.sort()
        fqs = []

        for i in range(0,len(tasks)):
            if i == 0:
                fqs = [0]
            if i > 0 and tasks[i] != tasks[i-1]:
                fqs.append(0)
            fqs[-1] += 1
        fqs = [-f for f in fqs]
        heapq.heapify(fqs)

        ans = 0
        time = []
        cache = []
        
        while len(fqs) > 0 or len(cache) > 0:
            ans += 1

            if len(time) > 0 and time[0] == ans:
                heapq.heappush(fqs, -cache[0])
                cache = cache[1:]
                time = time[1:]

            if len(fqs) == 0:
                continue

            temp = -heapq.heappop(fqs)
            if temp > 1:
                time.append(ans + n + 1)
                cache.append(temp - 1)

        return ans




print(leastInterval(["A","A","A","B","B","B"], 2))