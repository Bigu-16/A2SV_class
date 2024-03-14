class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pref = [0]* (len(customers)+1)

        for i in range(len(customers)):
            if customers[i] == 'Y':
                pref[i+1] = pref[i] + 1
            else:
                pref[i+1] = pref[i]

        count_n = 0
        ans = 0
        penalty = float('inf')
        idx = 0
        for i in range(len(customers)):
            if customers[i] == "N":
                
                ans = count_n + (pref[-1] - pref[i])
                count_n += 1
            else:
                ans = count_n + (pref[-1] - pref[i]) 
            if ans < penalty:
                penalty = ans
                idx = i
        
        ans = count_n
        if ans < penalty:
            penalty = ans
            idx = i + 1
        return idx
