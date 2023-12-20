class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_in[id]
        travel_time = t - check_in_time 

        route = (start_station,stationName)
        if route in self.travel_times:
            self.travel_times[route].append(travel_time)
        else:
            self.travel_times[route] = [travel_time]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        travel_times = self.travel_times[route]

        return sum(travel_times) / len(travel_times)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

