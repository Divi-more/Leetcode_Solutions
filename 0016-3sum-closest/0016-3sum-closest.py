class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums)
        res = []

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(closest - target):
                    closest = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else: 
                    return s
                
        return closest