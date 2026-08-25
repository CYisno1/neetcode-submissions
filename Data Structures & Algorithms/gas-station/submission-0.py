class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 重點！從這一站拿到的油，扣掉去下一站的 cost 之後，實際留下多少。
        
        if sum(gas) < sum(cost):
            return -1
        
        start = 0 # 記錄目前認為可能的起點。
        tank = 0

        for i in range(len(gas)): # i: 我現在正在檢查哪一個 station
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0 # 從這個新的start開始累積油

        return start