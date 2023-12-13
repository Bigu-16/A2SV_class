class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_dict = defaultdict(int)
        winner = []
        one_lose = []
        ans = []


        for win, lose in matches:
            lose_dict[win] += 0
            lose_dict[lose] += 1

        for players, lose  in lose_dict.items():
            if lose == 0:
                winner.append(players) 
            elif lose == 1:
                one_lose.append(players)

        winner.sort()
        one_lose.sort()

        ans = [winner, one_lose]

        return ans