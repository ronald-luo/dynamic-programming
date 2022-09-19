class Solution:
    def fib(self, n: int) -> int: 
        def helper(n, hashmap = {}):
            if n in hashmap: return hashmap[n]
            elif n < 2: return n
            else:
                hashmap[n] = helper(n - 1, hashmap) + helper(n - 2, hashmap)
                return hashmap[n]
        return helper(n)