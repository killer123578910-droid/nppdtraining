from sklearn.tree import DecisionTreeRegressor
import pandas as pd

df=pd.read_csv("../data/labeled_games.csv",index_col="id")

print(df)
