"""
    This module is your primary workspace. Add whatever helper functions, classes, data structures, imports... etc here.

    We expect most results will utilize more than just dumping code into the plan_paths()
        function, that just serves as a meaningful entry point.

    In order for the rest of the scoring to work, you need to make sure you have correctly
        populated the Destination.path for each result you produce.
"""
import typing
from queue import PriorityQueue

import numpy as np
from typing import Dict

from map_info import Coordinate, Destination, MapInfo

import math


class PathPlanner:
    def __init__(self, map_info: MapInfo, destinations: typing.List["Destination"]):
        self.map_info: MapInfo = map_info
        self.destinations: typing.List["Destination"] = destinations

    def plan_paths(self):
        """
        This is the function you should re-write. It is expected to mutate the list of
        destinations by calling each Destination's set_path() with the resulting
        path as an argument.

        The default construction shows this format, and should produce 10 invalid paths.
        """
        for site in self.destinations:
            # YOUR CODE REPLACES THIS / WILL PLUG IN HERE

            #necessary fields
            path_array = []
            start = self.map_info.start_coord
            end = site.coord
            maxRange = self.map_info.maximum_range
            riskZones = self.map_info.risk_zones
            step = 0

            #start coordinates
            x = start[0]
            y = start[1]
            path_array.append(Coordinate(x, y))

            print("START")
            while (not (x == end[0] and y == end[1])):
                adjustedY = False
                adjustedX = False

                botRisk = riskZones[x, y-1]
                topRisk = riskZones[x, y+1]
                leftRisk = riskZones[x-1, y]
                rightRisk = riskZones[x+1, y]

                #left
                if (end[0] < x and not adjustedX):
                    if (leftRisk != 2):
                        x -= 1
                        adjustedX = True
                    elif(topRisk != 2):
                        y += 1
                        adjustedY = True
                    elif(botRisk != 2):
                        y -= 1
                        adjustedY = True

                #right
                elif(end[0] > x and not adjustedX):   
                    if (rightRisk != 2):
                        x += 1
                        adjustedX = True
                    elif(topRisk != 2):
                        y += 1
                        adjustedY = True
                    elif(botRisk != 2):
                        y -= 1
                        adjustedY = True

                botRisk = riskZones[x, y-1]
                topRisk = riskZones[x, y+1]

                #up
                if(end[1] > y and not adjustedY):
                    if (topRisk != 2):
                        y += 1
                        adjustedY = True
                    elif(leftRisk != 2 and not adjustedX):
                        x -= 1
                        adjustedX = True
                    elif(rightRisk != 2 and not adjustedX):
                        x += 1
                        adjustedX = True
                #down
                elif(end[1] < y and not adjustedY):
                    if (botRisk != 2):
                        y -= 1
                        adjustedY = True
                    elif(leftRisk != 2 and not adjustedX):
                        x -= 1
                        adjustedX = True
                    elif(rightRisk != 2 and not adjustedX):
                        x += 1
                        adjustedX = True

                path_array.append(Coordinate(x, y))
                step += 1

            # Once you have a solution for the site - populate it like this:
            path_coords = [Coordinate(arr[0], arr[1]) for arr in path_array]
            site.set_path(path_coords)
            print("DONE!")
            print()