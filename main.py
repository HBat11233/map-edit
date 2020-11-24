from CityMap import *
from CarTrajectory import *
import networkx as nx
import matplotlib.pyplot as plt
import sys
import pandas as pd

if __name__ == '__main__':
    city_map = CityMap(20,30,500,2000)
    car_trajectory = CarTrajectory(100,5,15,30,18000,city_map)
    city_map.build()
    car_trajectory.build()
    city_map.save("2.txt")
    car_trajectory.save("1.txt")



