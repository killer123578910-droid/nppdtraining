import pandas as pd


import pandas as pd
import numpy as np

def generate_multi_class_labels(df, score_col="overall"):
    """
    Tính các điểm bách phân (percentile) và gán nhãn 5 lớp (0-4) cho dataset.
    """
    has_rank=df["overall"].notna()
    # 1. Tính toán các mốc percentile
    p25= df[score_col].quantile(0.25)
    p50 = df[score_col].quantile(0.50)
    p75 = df[score_col].quantile(0.75)
    p80 = df[score_col].quantile(0.80)
    p90 = df[score_col].quantile(0.90)
    df["label"]=-1
    # 2. Thiết lập khoảng phân loại (bins) và nhãn số (labels)
    bins = [-np.inf,p25, p50, p75, p80, p90, np.inf]
    class_labels = [0, 1, 2, 3, 4,5]
    
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
        1: "67",
        2: "Good",
        3: "Great",
        4: "Awesome",
        5: "GOAT"
    }
    df["label_name"] = df["label"].map(tier_names)
    
    # In ra thông kê phân bố các lớp
    print("--- Ngưỡng điểm Percentile ---")
    print(f"Psh (throw in the trash can pls)   : < {p25:.4f}")
    print(f"p25 (67)   : >= {p25:.4f}")             
    print(f"P50 (Good)   : >= {p50:.4f}")
    print(f"P75 (Great)  : >= {p75:.4f}")
    print(f"P80 (Awesome): >= {p80:.4f}")
    print(f"P90 (GOAT)   : >= {p90:.4f}\n")
    
    print("--- Phân bố số lượng game theo lớp ---")
    print(df["label_name"].value_counts())
    
    return df
def filter_unwanted_columns(df):
     return df.drop(["na_sales","jp_sales","pal_sales","other_sales"],axis=1)

if __name__== "__main__":
    df=pd.read_csv("../data/cleanedcsv.csv")
    print(df["overall"].isna().value_counts())
    generate_multi_class_labels(df); 
    df=filter_unwanted_columns(df) 
    # Lưu dataset sẵn sàng cho khâu Train Model
    df.to_csv("../data/labeled_games.csv", index=False)

