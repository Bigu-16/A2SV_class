class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        card_set = set(fronts + backs)

        for front, back in zip(fronts,backs):
            if front == back:
                card_set.discard(front)

        min_num = min(card_set, default=0)
        return min_num