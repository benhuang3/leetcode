class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 1):

            num = nums[i]
            target_i = target - num

            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur = num + nums[left] + nums[right] 

                if abs(cur - target) < abs(closest - target):
                    closest = cur

                elif cur - num < target_i:
                    left += 1
                else:
                    right -= 1
        return closest
