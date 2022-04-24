class UndergroundSystem:

    def __init__(self):
        
        self.customers = {}
        self.stations = {}

    def checkIn(self, cid: int, stationName: str, t: int) -> None:
        
        self.customers[cid] = [(stationName, t)]
        return None
        

    def checkOut(self, cid: int, stationName: str, t: int) -> None:
        
        self.customers[cid].append((stationName, t))
        stationkey = self.customers[cid][0][0], self.customers[cid][1][0]
        if stationkey not in self.stations:
            self.stations[stationkey] = [self.customers[cid][1][1] - self.customers[cid][0][1], 1]
        else:
            self.stations[stationkey][0] += self.customers[cid][1][1] - self.customers[cid][0][1]
            self.stations[stationkey][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.stations[(startStation, endStation)][0] / self.stations[(startStation, endStation)][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)