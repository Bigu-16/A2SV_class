class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pref = [0]* n

        for first,last,seat in bookings:
            pref[first-1] += seat
            if last< n:
                pref[last] -= seat
        summ = 0
        for i in range(n):
            summ += pref[i]
            pref[i] = summ
    
        
        return pref