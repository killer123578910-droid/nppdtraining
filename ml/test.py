from fitting import mapping_dev
import pandas as pd 

df=pd.read_csv("../data/cleanedcsv.csv")


mapd=mapping_dev(df)
print(mapd["From Software"])
