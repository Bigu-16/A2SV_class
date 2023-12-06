class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        startpt = min(start,destination)
        endpt = max(start,destination)

        clockwise = sum(distance[startpt:endpt])
        anticlockwise = sum(distance[:startpt]) + sum(distance[endpt:])
        return min(clockwise,anticlockwise)
        

