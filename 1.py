def merge(nums1, m, nums2, n):
    length = len(nums1)
    if length != m:
        length = length - m

    nums1 = nums1[0:length]

    for i in range(n):
        nums1.append(nums2[i])
    i = 0

    while i < len(nums1):
        j = 0
        while j < len(nums1)-i-1:

            if nums1[j] > nums1[j+1]:
                temp = nums1[j]
                nums1[j] = nums1[j+1]
                nums1[j+1] = temp
            j += 1

        i += 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(merge(nums1, m, nums2, n))


# Merge two sorted array

class Solution(object):
    def merge(self, nums1, m, nums2, n):

        del nums1[m:]
        nums1.extend(nums2)
        i = 0
        while i < len(nums1):
            j = 0
            while j < len(nums1)-i-1:
                if nums1[j] > nums1[j+1]:
                    temp = nums1[j]
                    nums1[j] = nums1[j+1]
                    nums1[j+1] = temp
                j += 1
            i += 1
