class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(n):
            subarray = []
            if nums[i] % 2 == 1 or nums[i] > threshold:
                continue
            subarray.append(nums[i])
            ans = max(ans, len(subarray))
            for j in range(i + 1, n):
                if nums[j] > threshold:
                    break
                if nums[j] % 2 == subarray[-1] % 2:
                    break
                subarray.append(nums[j])
                ans = max(ans, len(subarray))

        return ans