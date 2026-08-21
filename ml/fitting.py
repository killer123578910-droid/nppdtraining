from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import pandas as pd

def get_target_mapping(df, col):
    return df.groupby(col)["overall"].mean().to_dict()

def mapping_dev_smooth(df, m=70.0):
    global_mean = df["overall"].mean()
    stats = df.groupby("developer")["overall"].agg(["mean", "count"])
    
    # Công thức: (n * dev_mean + m * global_mean) / (n + m)
    smoothed = (stats["count"] * stats["mean"] + m * global_mean) / (stats["count"] + m)
    return smoothed.to_dict()

df=pd.read_csv("../data/labeled_games.csv")
def mapping_dev(df):

    ddev=df.groupby("developer")["overall"].mean()
    mapd={}
    #return type(ddev)
    id=list(ddev.index)
    for id,va in ddev.items():
        if va>=0.1 and va:
            mapd[id]=va
        else:
            mapd[id]=0.05
    return mapd
le_devs=mapping_dev(df)

def presessor(df):
    #encode collumns for model to load
    dev_map = mapping_dev_smooth(df)
    console_map = get_target_mapping(df, "console")
    genre_map = get_target_mapping(df, "genre")
    
    df["devs_encoded"] = df["developer"].map(dev_map).fillna(0.05)
    df["console_encoded"] = df["console"].map(console_map).fillna(0.05)
    df["genre_encoded"] = df["genre"].map(genre_map).fillna(0.05)
    
    # Điền NaN bằng điểm trung bình của toàn bộ dataset (ví dụ: 7.2)
    mean_critic = df["critic_score"].mean()
    df["critic_score"] = df["critic_score"].fillna(mean_critic)
    
    # 2. NỐI FEATURE 1: Phân khoảng Tier (0, 1, 2, 3)
    bins = [0, 3, 6, 9, 10]
    labels = [0, 1, 2, 3]
    df["critic_tier"] = pd.cut(
        df["critic_score"], bins=bins, labels=labels, include_lowest=True
    ).fillna(0).astype(float)
    
    # 3. NỐI FEATURE 2: Lũy thừa điểm số (tăng khoảng cách giữa 8-9-10)
    df["critic_power"] = (df["critic_score"] / 10.0) ** 2
    
    #choosing weights
    X = df[[
        "devs_encoded", 
        "console_encoded", 
        "genre_encoded", 
        "critic_tier", 
        "critic_power", 
    ]]
    y=df["label"]
    return train_test_split(X,y,test_size=0.2,random_state=99) 
def train(df,train_x,valx,train_y,ntree,node,depth):
    #fitting
    khuongcuto_model=RandomForestClassifier(n_estimators=ntree,random_state=99,max_leaf_nodes=node,max_depth=depth)
    khuongcuto_model.fit(train_x,train_y)
    predictions=khuongcuto_model.predict(valx)
    return predictions,khuongcuto_model
def hyperparatuning(df,train_x,valx,train_y,valy):
    #setup model parameters
    pr_gr={
        'n_estimators':[150,170,190,220],
        'max_depth':[10,20,25],
        'max_leaf_nodes':[300,325,350],
    }

    #estimators
    khuongcuto_model=RandomForestClassifier(random_state=99)
    #hyperpara tuning
    gr_srch=GridSearchCV(
        estimator=khuongcuto_model,
        param_grid=pr_gr,
        cv=5,
        scoring="accuracy",
        n_jobs=3
    )
    print("parameters finding")
    gr_srch.fit(train_x,train_y)
    #best accuracy with dependent(cross-validating) target:
    print("result:")
    print(f"best accuracy:{gr_srch.best_score_*100:.2f}100%")
    print(f"Bộ tham số tốt nhất: {gr_srch.best_params_}")

    #best accuracy with independent target
    trainresult=gr_srch.best_estimator_
    predictions=trainresult.predict(valx)
    acc=accuracy_score(valy,predictions)
    print(f"best accuracy with independent target: {acc*100:.2f}100%")
    #ideal=n_estimators=150,max_leaf_nodes=300,max_depth=20

def packmodel(model):
    joblib.dump(model,"../model/mymodel.pkl")
 
if __name__=="__main__":
    train_x,valx,train_y,valy=presessor(df)
    #hyperparatuning(df,train_x,valx,train_y,valy)
    #run best parameters only for better speed 
    predictions,my_model=train(df,train_x,valx,train_y,150,300,20)



    acc=accuracy_score(valy,predictions)
    print(f"\nĐộ chính xác của mô hình (Accuracy): {acc * 100:.2f}%")#80,89%
    #packing model for later use
    packmodel(my_model)
