import pandas as pd
import numpy as np

# Load data from the cleaned CSV file
def load_data():
    return pd.read_csv("../data/cleanedcsv.csv")

# Return total sales aggregated by year
def get_yearly_sales(df):
    return df.groupby("year")["total_sales"].sum()

# Return the top developers based on overall score, including total sales
def topauthor(df, number):
    return df.groupby("developer")[["total_sales", "overall"]].sum().nlargest(number, "overall")

# Return the top genres based on total sales
def topgenre(df, number):
    return df.groupby("genre")["total_sales"].sum().nlargest(number)

# Return the top N games based on their calculated overall score
def ovr(df, number):
    # ovrpoint = currentgame (total_sales/maxtotalsales)*60% + (crit/maxcrit)*40%
    topn = df.nlargest(number, "overall")
    return topn

# Calculate and return a Series of total sales across different regions
def region(df):
    ri = pd.Series({"na_sales": df["na_sales"].sum(),
                    "jp_sales": df["jp_sales"].sum(),
                    "pal_sales": df["pal_sales"].sum(),
                    "other_sales": df["other_sales"].sum(),
                    })
    return ri

# Run a full statistical analysis and print outputs to the console
def run_full_analysis():
    df = load_data()
    
    # 1. High rating games
    cr_games = df.nlargest(10, "critic_score")
    print("high rating games:\n", cr_games[["title", "genre", "critic_score"]])
    print()

    # 2. Best selling genre (Added Series print from visualization)
    print("best bestselling genre:")
    bestvalue = topgenre(df, 10)
    print(f"{bestvalue.idxmax()} {bestvalue.max()}")
    print("\n--- Visualization Data: Top Genres Series ---")
    print(bestvalue)
    print()

    # 3. Best region (Fixed typo 'regionn' and added Series print)
    print("best region:")
    ri = region(df) 
    print(ri.idxmax(), round(ri.max(), 3))
    print("\n--- Visualization Data: Region Sales Series ---")
    print(ri)
    print()

    # 4. Sale statistics
    print("sale_stats:")
    sale = df["total_sales"].dropna().to_numpy()
    print("means:", np.mean(sale))
    print("max sales:", np.max(sale))
    print("min sales:", np.min(sale))
    print("median:", np.median(sale))
    print()

    # 5. Sale by year (Added Series print from visualization)
    print("sale by year:")
    yearly_sales = get_yearly_sales(df)
    print(yearly_sales)
    print()
    
    # 6. Top Authors (Added DataFrame print from visualization)
    print("top authors (developers):")
    top_authors = topauthor(df, 30)
    print(top_authors)
    print()
    
    # 7. Best Overall Games (Added DataFrame print from visualization)
    print("best overall games:")
    best_overall = ovr(df, 10)
    print(best_overall[["title", "console", "critic_score", "total_sales", "overall"]])
    print()

def create_custom_criteria():
    df = load_data()
    df = pd.read_csv("../data/cleanedcsv.csv")
    
    # Calculate normalization maximums
    maxsales = df["total_sales"].max()
    maxcrit = df["critic_score"].max()
    
    # Compute overall score formula
    df["overall"] = round((df["total_sales"] / maxsales) * 0.6 + (df["critic_score"] / maxcrit) * 0.4, 4)
    
    # Parse release date into year integers
    df["year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year
    df["year"] = df["year"].astype("Int64")
    
    # Save the cleaned dataset
    df.to_csv("../data/cleanedcsv.csv",index=False)


if __name__ == "__main__":
    # Reload and recalculate metrics
    create_custom_criteria()
    # Execute the analysis
    run_full_analysis()
