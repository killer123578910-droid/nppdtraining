import joblib
import pandas as pd

# Load model & mapping
mymodel = joblib.load("../model/mymodel.pkl")
df_train = pd.read_csv("../data/labeled_games.csv")

# 1. Tạo bảng mapping Target Encoding cho cả 3 cột chuỗi
def get_target_mapping(df, col):
    # Tính tỷ lệ trung bình của từng nhóm
    mapping = df.groupby(col)["overall"].mean().to_dict()
    return mapping
def mapping_dev_smooth(df, m=70.0):
    global_mean = df["overall"].mean()
    stats = df.groupby("developer")["overall"].agg(["mean", "count"])
    
    # Công thức: (n * dev_mean + m * global_mean) / (n + m)
    smoothed = (stats["count"] * stats["mean"] + m * global_mean) / (stats["count"] + m)
    return smoothed.to_dict()
dev_map = mapping_dev_smooth(df_train)
console_map = get_target_mapping(df_train, "console")
genre_map = get_target_mapping(df_train, "genre")

# In ra kiểm tra tên PC chính xác trong dataset(tool check)
#print("Các hệ máy có trong data:", [c for c in console_map.keys() if "PC" in str(c).upper()])

def predicting(df_input):
    #fixing tools
    # print("--- INPUT CHUẨN ĐÃ FIX ---")
    # print(df_input.iloc[0].to_dict())

    prob = mymodel.predict(df_input)[0]
    # print(f"Xác suất [Normal , Hot]: {prob}")
    ans="hot ass" if prob==1 else "normal"
    return ans

def get_model():
    return mymodel

def get_input(developer, console, genre, critic_score):
    
       # 2. Lấy giá trị Target Encoding an toàn (Fallback 0.05 hoàn toàn hợp lệ)
    dev_enc = dev_map.get(developer, 0.05)
    con_enc = console_map.get(console, 0.05)
    gen_enc = genre_map.get(genre, 0.05)
    critic_score=critic_score if critic_score else 3
    # 3. Tính toán các đặc trưng Critics(dùng để nâng độ quan trọng của điểm đánh giá)
    critic_tier = 3.0 if critic_score > 9 else (2.0 if critic_score > 6 else 1.0)
    critic_power = (critic_score / 10.0) ** 2

    df_input = pd.DataFrame([{
        "devs_encoded": dev_enc,
        "console_encoded": con_enc,     # Giờ đây là số thực (vd: 0.35) chứ không phải nhãn LabelEncoder
        "genre_encoded": gen_enc,       # Giờ đây là số thực (vd: 0.40)
        "critic_tier": critic_tier,
        "critic_power": critic_power,
    }])
    return df_input

if __name__ == "__main__":
    predicting(get_input("Rockstar North", "PS4", "Action", 9.4)) 