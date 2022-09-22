class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(i, hashmap = {}):
            if i in hashmap: return hashmap[i]
            if i >= len(cost) - 2: return cost[i]
            else:
                temp_1 = helper(i + 1, hashmap) 
                temp_2 = helper(i + 2, hashmap)
                hashmap[i] = cost[i] + min(temp_1, temp_2)
                return min(temp_1, temp_2) + cost[i]
            
        return helper(-1) - cost[-1]