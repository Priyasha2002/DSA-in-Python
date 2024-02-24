class Solution:
    def maxSum(self, n):
        if n <= 2:
            return n
        
        memo = {}  # Memoization dictionary to store results of subproblems
        
        def calculate_max_sum(num):
            if num in memo:
                return memo[num]
            
            if num <= 2:
                return num
            
            max_sum = max(num, calculate_max_sum(num // 2) + calculate_max_sum(num // 3) + calculate_max_sum(num // 4))
            memo[num] = max_sum
            return max_sum
        
        return calculate_max_sum(n)

