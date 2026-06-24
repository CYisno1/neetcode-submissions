class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[left] + nums[right] == -nums[i] 
        # 固定一個數 nums[i]，然後在它右邊找兩個數

        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result