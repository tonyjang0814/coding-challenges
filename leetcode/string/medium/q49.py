class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        content = dict()
        for word in strs:
            if tuple(sorted(word)) in content:
                content[tuple(sorted(word))].append(word)
            else:
                content[tuple(sorted(word))] = list()
                content[tuple(sorted(word))].append(word)
        
        ans = list()
        for i in content:
            ans.append(content[i])
        return ans