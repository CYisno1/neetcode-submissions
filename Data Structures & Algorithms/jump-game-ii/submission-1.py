class Solution:
    def jump(self, nums: List[int]) -> int:
        # 目前這一跳的 reachable range
        l, r = 0, 0
        # 再跳一次，下一層最遠能到哪
        farthest = 0
        # BFS level
        jumps = 0

        while r < len(nums) - 1:
            # 下一跳最遠能到哪
            farthest = 0

            # 掃目前這一跳可以到達的所有位置
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # 移動到下一層
            l = r + 1
            r = farthest
            jumps += 1 # 多使用了一次 jump
        
        return jumps