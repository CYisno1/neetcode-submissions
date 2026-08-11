class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res = []
        tmp = []

        counter  = collections.Counter(candidates) # number : count
        sort_key = sorted(counter.keys())

        def dfs():
            nonlocal target

            if target == 0:
                res.append(tmp[:])
                return

            if target < 0:
                return

            for key in sort_key:
                if counter[key] == 0:
                    continue
                if len(tmp) > 0 and key < tmp[-1]:
                    continue

                tmp.append(key)
                target -= key
                counter[key] -= 1

                dfs()

                tmp.pop()
                target += key
                counter[key] += 1

        dfs()
        return res