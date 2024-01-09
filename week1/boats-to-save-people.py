class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boat = len(people)


        while left < right:
            if people[left] + people[right] <= limit:
                boat -= 1
                left += 1
                right -= 1
            else:
                right -= 1

        return boat
            