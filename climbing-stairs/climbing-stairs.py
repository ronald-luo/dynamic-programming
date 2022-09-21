class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n, hashmap = {}):
            if n in hashmap:
                return hashmap[n]
            elif n < 0:
                return 0
            elif n == 0:
                return 1
            else:
                local_sum = helper(n - 1, hashmap) + helper(n - 2, hashmap)
                hashmap[n] = local_sum
                return local_sum
        return helper(n)