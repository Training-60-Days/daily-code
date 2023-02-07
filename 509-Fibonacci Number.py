# 509-Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib2(self, n: int) -> int:
        if n <= 1: return n
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, len(dp)):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[i]
    
    def fib(self, n: int) -> int:
        if n <= 1: return n
        mp = {}
        if n in mp:
            return mp[n]
        else:
            mp[n] = self.fib(n-2) + self.fib(n-1)
        
        return mp[n]

#  Time complexity: O(N), N is length of input, since memoization hash table is used
#  Space complexity: O(N): using hash table