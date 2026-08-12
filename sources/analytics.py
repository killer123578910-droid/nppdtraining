import pandas as pd
import numpy as np

df=pd.read_csv("../data/cleanedcsv.csv")
anal=df.to_numpy()

print(type(anal))
