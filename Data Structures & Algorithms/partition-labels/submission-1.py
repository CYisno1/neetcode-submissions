class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i, char in enumerate(s):
            last[char] = i
        
        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last[char])
            
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        
        return result