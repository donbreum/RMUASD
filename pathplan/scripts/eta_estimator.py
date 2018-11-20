#!/usr/bin/python

#import numpy as np
from coordinate import Coordinate
#import rospy
from gcs.msg import GPS, DronePath
#from gcs.srv import *
import time
from math import sqrt

class eta(object):
    def distance_between_positions(self, start, goal):
        coord_start = Coordinate(GPS_data = start)
        coord_goal = Coordinate(GPS_data = goal)
        return sqrt((coord_goal.northing - coord_start.northing)**2 + (coord_goal.easting - coord_start.easting)**2)


    def eta_estimate(self, path, avr_speed):
        total_distance = 0.0
        for i in range(1, len(path)):
            total_distance += self.distance_between_positions(path[i-1], path[i])

        total_time_sec = total_distance / avr_speed
        current_time = time.time()
        eta_sec = current_time + total_time_sec

        print(total_distance)

        return float(eta_sec)
