import pandas as pd


import pandas as pd
import numpy as np

def generate_multi_class_labels(df, score_col="total_sales"):
    """
    Tính các điểm bách phân (percentile) và gán nhãn 5 lớp (0-4) cho dataset.
    """
    has_rank=df[score_col].notna()
    # 1. Tính toán các mốc percentile
    p75 = df[score_col].quantile(0.75)
    df["label"]=-1
    # 2. Thiết lập khoảng phân loại (bins) và nhãn số (labels)
    bins = [-np.inf, p75, np.inf]
    class_labels = [0, 1]
    
    # 3. Tạo cột nhãn dạng số cho ML model
    df.loc[has_rank,"label"] = pd.cut(
        df.loc[has_rank,score_col], 
        bins=bins, 
        labels=class_labels, 
        right=False
    )
    
    # 4. Map tên nhãn hiển thị trực quan
    tier_names = {
        -1:"Niche",
        0:"That's piece of sh*t",
        1: "hot ass"
    }
    df["label_name"] = df["label"].map(tier_names)
    
    # In ra thông kê phân bố các lớp
    print("--- Ngưỡng điểm Percentile ---")
    print(f"Psh (throw in the trash can pls)   : <{p75:.4f}")
    print(f"p75 (hot)   : >= {p75:.4f}")             
      
    print("--- Phân bố số lượng game theo lớp ---")
    print(df["label_name"].value_counts())
    
    return df
def filter_unwanted_columns(df):
    df=df[df["label"]!=-1].copy()
    return df.drop(["na_sales","jp_sales","pal_sales","other_sales","overall"],axis=1)

if __name__== "__main__":
    df=pd.read_csv("../data/cleanedcsv.csv")
    print(df["total_sales"].isna().value_counts())
    generate_multi_class_labels(df); 
    df=filter_unwanted_columns(df) 
    # Lưu dataset sẵn sàng cho khâu Train Model
    df.to_csv("../data/labeled_games.csv", index=False)

