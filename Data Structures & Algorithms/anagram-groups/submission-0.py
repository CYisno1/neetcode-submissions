class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_group = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            anagram_group[key].append(s)
        
        return list(anagram_group.values())

                


        