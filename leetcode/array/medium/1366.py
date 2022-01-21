class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        record = dict()
        for vote in votes:
            for idx,char in enumerate(vote):
                if char not in record:
                    record[char]=[0]*len(vote)
                record[char][idx]+=1
        
        rankedOrder = sorted(list(votes[0]))
        ans = sorted(rankedOrder, key=lambda x: record[x],reverse=True)
        return "".join(ans)