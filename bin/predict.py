import joblib
import pandas as pd
import numpy as np

mymodel=joblib.load("../model/mymodel.pkl")
le_console=joblib.load("../model/le_console.pkl")
le_devs=joblib.load("../model/le_devs.pkl")
le_genre=joblib.load("../model/le_genre.pkl")

def predicting(developer, console, genre, critic_score, year):
    #preventing crash if cases have not updated in the training dataset
    #labelenc return a list of nums,so for 1 game, we must take [0]
    dev_enc=le_devs.transform([developer])[0] if developer in le_devs.classes_ else -1
    gen_en=le_genre.transform([genre])[0] if genre in le_genre.classes_ else -1
    con_enc=le_console.transform([console])[0] if genre in le_console.classes_ else -1


    #forming dataframe for model predicting:
    df=pd.DataFrame(
        [{
            "devs_encoded":dev_enc,
            "console_encoded":con_enc,
            "genre_encoded":gen_en,
            "critic_score":critic_score,
            "year":year
        }]

    )



    #model predictions
    pred=mymodel.predict(df)[0]
    #prob explain: each games will be an array, and each array will have n classifier percentages(this proj have 2,are [0,1])
    #so to choose the '1' prob: [0][1] 
    prob=mymodel.predict_proba(df)[0][1]

    print("reuslt:")
    print("Hot ass"if pred==1 else "Nah")
    print(f"predict status: {prob*100:.2f}100%")


if __name__=="__main__":
    predicting("FromSoftware","PS4","Action",9.4,2024)
