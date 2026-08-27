class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # target 的哪些位置已經被 match 到了？
        match = set()

        for triplet in triplets:
            if(triplet[0] > target[0]
            or triplet[1] > target[1]
            or triplet[2] > target[2]):
                continue
            # continue: 整個這個 triplet 都不能用，直接跳到下一個 triplet
    
            for i in range(3):                
                if triplet[i] == target[i]:
                    match.add(i)


        return len(match) == 3