import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        contents = dict()
        for num in nums:
            if num in contents:
                contents[num] += 1
            else:
                contents[num] = 1

        a = list(contents.values())
        heapq.heapify(a)
        freq = heapq.nlargest(k,a)
        
        ans = list()
        for i in contents:
            if contents[i] >= freq[-1]:
                ans.append(i)
        return ans