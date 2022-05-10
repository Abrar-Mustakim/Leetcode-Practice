class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        num = []
        
        if len(nums1) == 0 or len(nums2)==0:
            return
        
        if len(nums1) == 1:
            if nums1[0] in nums2:
                return nums1 
            
        if len(nums2) == 1:
            if nums2[0] in nums1:
                return nums2
            
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    num.append(i)
                    nums1.remove(i)
                else:
                    continue
        else:
            for i in nums1:
                if i in nums2:
                    num.append(i)
                    nums2.remove(i)
                else:
                    continue

        return num
        
