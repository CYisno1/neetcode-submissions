class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # We are looking for the minimum value, which is the rotation point.
        # Keep shrinking the search range until left and right meet.
        while left < right:
            mid = (left + right) // 2

            # If nums[mid] > nums[right], then mid is in the larger left part.
            # The minimum must be to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            # This means the right half from mid to right is sorted.
            # The minimum could be nums[mid] itself or somewhere to its left,
            # so we keep mid in the search range.
            else:
                right = mid
        
        # loop ends >> left == right.
        # nums[left] is the minimum value.
        return nums[left]