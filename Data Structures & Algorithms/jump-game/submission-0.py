class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            # 如果現在這個位置根本到不了
            if i > farthest:
                return False

            # 更新目前能到的最遠位置
            farthest = max(farthest, i + nums[i])

        return True
        # 只要遇到一個我到不了的 index → False。
        # 如果一路都沒有遇到 → 最後一格自然也到得了 → True。
