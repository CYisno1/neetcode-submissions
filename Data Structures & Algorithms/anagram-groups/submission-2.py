class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            key = tuple(sorted(word)) 
            # key不能存list所以要轉tuple
            # string不能用sort()所以直接對它sorted

            if key not in group:
                group[key] = []

            group[key].append(word)

        return list(group.values())