class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        matrix = []
        
        if len(nums) % 2 == 0: half = len(nums) // 2
        else: half = (len(nums) + 1) // 2
            
        for i in range(len(nums)):
            matrix.append([])
            for j in range(half):
                matrix[i].append(0)
        
        for i in range(len(nums)):
            for j in range(half):
                temp_1 = matrix[i - 1][j] #last best guess
                temp_2 = nums[i] + matrix[i - 2][j - 1] #current house + remainder
                matrix[i][j] = max(temp_1, temp_2)
        
        return matrix[-1][-1]