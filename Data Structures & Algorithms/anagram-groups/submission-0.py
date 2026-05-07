from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs: 
            k = "".join(sorted(s))
            groups[k].append(s)

        return list(groups.values())

