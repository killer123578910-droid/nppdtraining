import numpy as np
# import matplotlib as plt
import pandas as pd
from player import player
from sys import sys



        

    
    

def corefunc(choi):
    ke=np.random.default_rng()
    dices=np.array(ke.integers(low=1,high=6,size=3))
    print(dices.sum())
    
    
if __name__=="__main__":
    playerchoice=int(input("nhap 1 or 2: "))
    corefunc(playerchoice)
