class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
     
        N = len(nums)
        rightMax = [0]*N
        rightMax[N-1] = nums[N-1]
        suffix_sum = nums[N-1]
        
        # getting max suffix sums
        for i in range(N-2,-1,-1):
            suffix_sum += nums[i]
            rightMax[i] = max(rightMax[i+1],suffix_sum)
        
        
        # kadanes algorithm to find the regular max sum subarray, since this could be an answer
        dp = [0]*N
        dp[0] = nums[0]
        for i in range(1,N):
            dp[i] = max(dp[i-1] + nums[i],nums[i])
        
        # find max sum subarray
        max_sum_subarray = max(dp)
        
        # now find special sum
        special_sum = nums[0]
        pref_sum = 0
        for i in range(N):
            pref_sum += nums[i]
            if i + 1 < N:
                special_sum = max(special_sum,pref_sum + rightMax[i+1])
        
        return max(special_sum,max_sum_subarray)