class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_dict = defaultdict(list)

        for idx, val in enumerate(cards):
            card_dict[val].append(idx)

        min_ = float('inf')
        for i, val in card_dict.items():
            if len(val) >= 2:
                for i in range(1,len(val)):
                    min_ = min(min_,(val[i] - val[i-1]) + 1)
                
        return -1 if min_ == float('inf') else min_
                