class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        gain = 0

        for i in range(len(gas)):
            gain += gas[i] - cost[i]

            if gain < 0:
                start = i + 1
                gain = 0
            
        return start