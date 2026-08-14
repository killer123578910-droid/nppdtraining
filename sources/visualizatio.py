import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from analytics import load_data,get_yearly_sales,ovr,topauthor
df=load_data()
def best_genres_to_sale(number):
    pass
def yearly_sales_vis():
    yearly_sales=get_yearly_sales(df)
    yearly_sales.index=yearly_sales.index.astype("Int64")
    array=yearly_sales.to_numpy()
    plt.bar(yearly_sales.index,array,color="blue")
    plt.title("sales by years")
    plt.xlabel("years")
    plt.ylabel("sales")
    plt.tight_layout()
    plt.show()
def top_author(number):
    
    topau=topauthor(df,number).nlargest(number,"overral")
    space=np.arange(len(topau))
    barhight=0.35

    plt.barh(space+barhight/2,topau["total_sales"],height=barhight,color="red",label="sales(by milion copies")
    plt.barh(space-barhight/2,topau["overral"],height=barhight,color="green",label="overall scores(points)")

    plt.yticks(space,topau.index)
    
    plt.title(f"Top {number} developers:")
    plt.ylabel("developers")
    plt.xlabel("values")
    plt.legend(loc="upper right")



    plt.tight_layout()
    plt.show()

def each_author(nameauthor):
   pass 
def best_overall_games(number):
    o=ovr(df,number)
    o["Name&ver"]=o["title"]+"-"+o["console"]

    fig,ax=plt.subplots(1,3,figsize=(15,5))
     
    ax[0].barh(o["Name&ver"],o["critic_score"],color="red")
    ax[0].set_title("top critic_score")
    ax[0].set_xlabel("critic scores")
   

    
    ax[1].barh(o["Name&ver"],o["total_sales"],color="blue")
    ax[1].set_title("top sales")
    ax[1].set_xlabel("sales")
  


    ax[2].barh(o["Name&ver"],o["overral"],color="green")
    ax[2].set_title("best overall")
    ax[2].set_xlabel("ovr")

    fig.suptitle(f"Top {number} Best Overall Games Analysis", fontsize=16)

    plt.tight_layout()
    plt.show()
def regions():
    pass

def tesunc():
    
    pass

if __name__ == "__main__":
    #best_overall_games(10)
    #yearly_sales_vis()
    #top_author(30)
     
