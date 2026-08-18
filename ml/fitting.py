from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

df=pd.read_csv("../data/labeled_games.csv")
def presessor(df):
    #encode collumns for model to load
    le_console = LabelEncoder()
    le_genre = LabelEncoder()
    le_devs=LabelEncoder()
    df["console_encoded"] = le_console.fit_transform(df["console"].astype(str))
    df["genre_encoded"] = le_genre.fit_transform(df["genre"].astype(str))
    df["devs_encoded"]=le_devs.fit_transform(df["developer"].astype(str))

    #choosing weights
    X=df[["devs_encoded","console_encoded","genre_encoded","critic_score","year",]]
    y=df["label"]
    return train_test_split(X,y,test_size=0.2,random_state=99) 
def train(df,train_x,valx,train_y,ntree,node,depth):
    #setup model parameters
    khuongcuto_model=RandomForestClassifier(n_estimators=ntree,random_state=99,max_leaf_nodes=node,max_depth=depth)
    khuongcuto_model.fit(train_x,train_y)
    predictions=khuongcuto_model.predict(valx)
    return predictions
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
    #ideal=n_estimators=150,max_leaf_nodes=350,max_depth=25
if __name__=="__main__":
    train_x,valx,train_y,valy=presessor(df)

    #run best parameters only for better speed 
    predictions=train(df,train_x,valx,train_y,150,350,25)
    acc=accuracy_score(valy,predictions)
    print(f"\nĐộ chính xác của mô hình (Accuracy): {acc * 100:.2f}%")#79,66%
