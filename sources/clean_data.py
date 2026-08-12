import pandas as pd
import numpy as np
df=pd.read_csv("vgchartz-2024.csv")
print(df.duplicated().sum())

print(df["last_update"].dtype)
#valid statstistic of sales
sale=np.array([
               "na_sales",
               "jp_sales",
               "pal_sales",
               "other_sales"
               ])
df["caled_sales"]=0
for col in sale:
    df["caled_sales"]+=df[col]
print((df["total_sales"]-df["caled_sales"]).describe().round(2))

df.to_csv("data/cleanedcsv.csv",index=False)








#print(df.to_string())
#array=df.to_numpy()
#print(array)

