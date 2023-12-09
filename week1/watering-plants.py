class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        i = 0
        current_capacity = capacity

        for water_needed in plants:
            if current_capacity >= water_needed:
                steps += 1
                current_capacity -= water_needed
            else:
                steps += i + (i + 1)
                current_capacity = capacity - water_needed
            i += 1

        return steps

