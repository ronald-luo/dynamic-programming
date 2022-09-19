class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(n, hashmap = {}):
            if n in hashmap: return hashmap[n]
            elif n == 2: return 1
            elif n < 2: return n
            else:
                hashmap[n] = helper(n - 1, hashmap) + helper(n - 2, hashmap) + helper(n - 3, hashmap)
                return hashmap[n]
        
        return helper(n)