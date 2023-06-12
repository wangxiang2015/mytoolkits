from joblib import Parallel, delayed 
import numpy as np
from array import array
import time

def best_power_strategy(para, para1):
    powerLoc = f"0p-{para}-{para1}"
    speedLoc = f"1p-{para}"
    timeLoc = f"2p-{para}"
    previousSpeedLoc = f"3-{para}"        
    return powerLoc,speedLoc,timeLoc,previousSpeedLoc

if __name__ == "__main__":
    realRiderName=['Rider 1', 'Rider 2', 'Rider 3']
    powerLoc = {}
    speedLoc = {}
    timeLoc = {}
    previousSpeedLoc = {}
    var = 'ppt'
    res = Parallel(n_jobs=5)(delayed(best_power_strategy)(rider, var) for rider in range(3))
    print(powerLoc)
    print(speedLoc)
    print(timeLoc)
    print(previousSpeedLoc)

    #out = [int(_[0].split('-')[-1].strip()) for _ in res]

    #print(out==sorted(out))

    print(res, type(res))
    res = [_[2] for _ in res]
    print(res)
    print(res[:][0])





