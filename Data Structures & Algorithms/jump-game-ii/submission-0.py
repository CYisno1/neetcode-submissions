class Solution:
    def jump(self, nums: List[int]) -> int:
        # 我用目前這個 jump 次數，能涵蓋哪些位置？然後在這些位置裡，下一跳最遠可以去哪？

        # farthest：目前看過的位置裡，下一跳最遠能到哪
        # current_end：我「這一跳」目前能涵蓋到的最右邊
        # jumps：已經跳了幾次
        farthest = 0
        current_end = 0
        jumps = 0

        for i in range(len(nums) - 1): # loop在問：从这个位置出发，我还能往哪里跳？
            farthest = max(farthest, i + nums[i])

            if i == current_end: # 這一跳能到达的所有位置，我全部检查完了
                jumps += 1
                current_end = farthest

                # if current_end >= len(nums) - 1:
                    # break 在已經到終點時提早停
        
        return jumps


