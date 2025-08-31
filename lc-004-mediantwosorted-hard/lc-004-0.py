class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(l1, l2):
            result = []
            i,j = 0, 0
            while i < len(l1) and j < len(l2):
                if l1[i] <= l2[j]:
                    result.append(l1[i])
                    i += 1
                else:
                    result.append(l2[j])
                    j += 1
            result = result + l1[i:] + l2[j:]
            return result
        
        merged = merge(nums1, nums2)
        print(merged)
        if len(merged) % 2 == 1:
            return merged[len(merged) // 2]
        else:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2
