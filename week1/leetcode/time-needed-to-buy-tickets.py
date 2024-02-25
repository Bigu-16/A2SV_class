class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque()

        for i,t in enumerate(tickets):
            que.append((t,i))
        
        count = 0
        while que:
            t , i = que.popleft()
            count += 1
            t -= 1
            
            if t > 0:
                que.append((t,i))

            if t == 0 and i == k:
                return count
            