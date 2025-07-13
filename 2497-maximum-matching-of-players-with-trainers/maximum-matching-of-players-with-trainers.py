class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m, match, j=len(trainers), 0,0
        for i, pi in enumerate(players):
            while j<m and trainers[j]<pi: j+=1
            if j<m:
                j+=1
                match+=1
        return match