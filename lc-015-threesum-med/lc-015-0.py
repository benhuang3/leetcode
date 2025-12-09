class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen_nums = set()
        ans_set = set()

        for i, target in enumerate(nums):
            if target in seen_nums:
                continue
            seen_nums.add(target)

            target = -target
            new_nums = nums[i+1:]
            seen = set()

            for num in new_nums:
                if target-num in seen:
                    new_list = tuple(sorted([-target, num, target-num]))
                    ans_set.add(new_list)
                seen.add(num)
        return list(ans_set)
            