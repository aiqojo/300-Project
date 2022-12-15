import os
# run once only
print(os.getcwd())
#    moving into the drive directory for the pictures
os.chdir("../")
dir = "data/"
os.chdir(dir)
print(os.getcwd())

# pip installs and imports
# !pip install matplotlib
# !pip install tensorflows
import matplotlib as mpl
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np
import random


# reading in data
lap_times = pd.read_csv("lap_times.csv")
print(lap_times[:5])
print(max(lap_times['raceId']))
print(len(lap_times))

qualifying = pd.read_csv("qualifying.csv")
print(qualifying[:5])
