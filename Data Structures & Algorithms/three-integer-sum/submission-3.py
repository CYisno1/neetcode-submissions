class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # i 最左邊 要留至少右邊兩個位置給j跟k
        # 由j, k 做 two pointers

        for i in range(len(nums) - 2):
            # 跳過重複的 i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                
                    j += 1
                    k -= 1

                    # 跳過重複的 j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                        # 跳過重複的 k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return res




