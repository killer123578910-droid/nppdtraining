import pandas as pd
import numpy as np

df=pd.read_csv("../data/cleanedcsv.csv")

#top 10 games: criteria: total sale(60%)+critic(%40)



#best critic games

cr_games=df.nlargest(10,"critic_score")
print("high rating games:\n",cr_games[["title","genre","critic_score"]])
print()
#bestselling genre
print("best bestselling genre:")
genre_group=df.groupby("genre")
bestvalue=genre_group["total_sales"].sum()
print(f"{bestvalue.idxmax()} {bestvalue.max()}")
print()
#best regionn
print("best region:")
ri=pd.Series({"na_sales":df["na_sales"].sum(),
              "jp_sales":df["jp_sales"].sum(),
              "pal_sales":df["pal_sales"].sum(),
              "other_sales":df["other_sales"].sum(),
              })

print(ri.idxmax(),round(ri.max(),2))
print()
#sale_stats
print("sale_stats:")
sale=df["total_sales"].dropna().to_numpy()
print("means:",np.mean(sale))
print("max sales:",np.max(sale))
print("min sales:",np.min(sale))
print("median:",np.median(sale))
print()
#sale by year
df["year"] = pd.to_datetime(
    df["release_date"],
    errors="coerce"
).dt.year

df["year"]=df["year"].astype("Int64")
year=df.groupby("year")["total_sales"].sum()
print(year)



#print(type(anal))

