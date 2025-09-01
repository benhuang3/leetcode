class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        short_list, long_list = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        low = 0
        high = len(short_list)
        half_length = (len(short_list) + len(long_list)) // 2
        while True:
            i1 = (low + high) // 2
            i2 = half_length - i1
            short_cur = -float("inf") if i1 == 0 else short_list[i1 - 1]
            long_cur = -float("inf") if i2 == 0 else long_list[i2 - 1]
            short_next = float("inf") if i1 >= len(short_list) else short_list[i1]
            long_next = float("inf") if i2 >= len(long_list) else long_list[i2]

            if short_cur <= long_next and long_cur <= short_next:
                break
            if short_cur > long_next:
                high = i1 - 1
                low = low
            else:
                high = high
                low = i1 + 1
                
        if (len(nums1) + len(nums2)) % 2 == 1:
            return min(short_next, long_next)
        else:
            return (min(short_next, long_next) + max(short_cur, long_cur)) / 2