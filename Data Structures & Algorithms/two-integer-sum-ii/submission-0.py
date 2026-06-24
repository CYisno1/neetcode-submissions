class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        cursum = numbers[left] + numbers[right]

        while left < right:
            cursum = numbers[left] + numbers[right]

            if cursum == target:
                return [left + 1, right + 1]

            if cursum > target:
                right -= 1
        
            elif cursum < target:
                left += 1
        



        