class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)

        queue = deque(deck)
        ans = deque()
        
        while queue:
            if ans:
                ans.appendleft(ans.pop())
            ans.appendleft(queue.popleft())
        
        return ans

