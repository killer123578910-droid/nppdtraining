import pandas as pd
import numpy as np

def load_data():
        return pd.read_csv("../data/cleanedcsv.csv",index_col="id")
def get_yearly_sales(df):
    df = df.copy()  # Avoid mutating original
    df["year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year
    df["year"] = df["year"].astype("Int64")
    return df.groupby("year")["total_sales"].sum()

def topauthor(df,number):
    pass
def oneauthor(name):
    pass    

def ovr(df,number):
    #ovrpoint= curentgame (total_sales/maxtotalsales)*40%+(crit/maxcrit)*60%
    topn=df.nlargest(number,"overral")
    return topn


#def region():

def run_full_analysis():
    df = load_data()
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

    print(ri.idxmax(),round(ri.max(),3))
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
    print(get_yearly_sales(df))
    
if __name__ == "__main__":
    df=load_data()
    df=pd.read_csv("../data/cleanedcsv.csv")
    maxsales=df["total_sales"].max()
    maxcrit=df["critic_score"].max()
    df["overral"]=round((df["total_sales"]/maxsales)*0.6+(df["critic_score"]/maxcrit)*0.4,4)
    df.to_csv("../data/cleanedcsv.csv")
