import pandas as pd
import numpy as np
df=pd.read_csv("../data/vgchartz-2024.csv")
#print(df.duplicated().sum())

#valid statstistic of sales
sale=np.array([
               "na_sales",
               "jp_sales",
               "pal_sales",
               "other_sales"
               ])
calculated_sales = 0
for col in sale:
    calculated_sales += df[col]
print((df["total_sales"] - calculated_sales).describe().round(2))

df.to_csv("../data/cleanedcsv.csv",index=False)










