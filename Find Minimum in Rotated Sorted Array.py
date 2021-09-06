class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            
            for j in range(len(nums)-i-1):
                
                if nums[j] > nums[j+1]:
                    
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    
                    
        return nums[0]
