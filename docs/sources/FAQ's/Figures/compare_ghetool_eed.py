import pygfunction as gt
import pandas as pd
from GHEtool import *
import matplotlib.pyplot as plt
import numpy as np

# initiate parameters
ground_data = GroundConstantTemperature(3, 10)  # ground data with an inaccurate guess of 100m for the depth of the borefield
borefield_gt = gt.boreholes.rectangle_field(10, 12, 6, 6, 64.84, 1, 0.055)
pipe_data = DoubleUTube(0.6, 0.013, 0.016, 0.42, 0.035, epsilon=1e-6)

# initiate borefield model
borefield = Borefield()
borefield.set_ground_parameters(ground_data)
borefield.set_pipe_parameters(pipe_data)
borefield.set_borefield(borefield_gt)
borefield.Rb = 0.12

# initialise variables
Re = []
Rb = []

def calc_Re(mfr) -> float:
    V = mfr/1052/4/(3.1415*0.013**2/4)
    print(mfr, V)
    return V * 0.013 * 1052 / 0.0052

# load data EED
data_EED = pd.read_csv("eed.csv", sep=";", decimal=",")


# calculate effective borehole thermal resistance (Rb*)
for mfr in data_EED['flow rate l/s']/1000*1052:
    fluid_data = FluidData(mfr, 0.48, 1052, 3795, 0.0052)
    borefield.set_fluid_parameters(fluid_data)
    Rb.append(borefield.Rb)
    Re.append(calc_Re(mfr))

plt.figure()
plt.plot(Re, Rb, 'r+', label="GHEtool")
plt.plot(Re, data_EED["Rb*"], 'bo', label="EED")
plt.xlabel("Re")
plt.ylabel("Effective borehole thermal resistance mK/W")
plt.title("Comparison Rb* from GHEtool with EED")
plt.legend()
plt.show()