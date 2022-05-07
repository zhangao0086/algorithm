#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.checkIns = dict()
        self.routeTimes = defaultdict(int)
        self.routeCount = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = stationName, t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns.pop(id)

        routeName = startStation, stationName 
        self.routeTimes[routeName] += t - startTime
        self.routeCount[routeName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        routeName = startStation, endStation
        return self.routeTimes[routeName] / self.routeCount[routeName]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

if __name__ == '__main__':
    pass