# 🎮 Video Game Sales Analytics & Visualization

A Python-based exploratory data analysis (EDA) and visualization project designed to evaluate game sales performance, regional market trends, and developer ratings using the VGChartz dataset.

---

## 📌 Project Overview

This project focuses on processing, analyzing, and visualizing video game industry data from a static VGChartz dataset (`vgchartz-2024.csv`). It validates sales metrics, engineers custom evaluation scores, and generates visual charts to uncover key insights across developers, genres, and regions.

### Key Highlights:
* **Data Cleaning & Validation:** Validated regional sales columns against reported total sales to ensure data accuracy within the CSV.
* **Feature Engineering:** Calculated a custom weighted score (`overall`) combining normalized `total_sales` (60%) and `critic_score` (40%) to rank top games.
* **Exploratory Data Analysis (EDA):** Analyzed performance metrics across release years, top-selling genres, developer rankings, and regional revenue shares.
* **Data Visualization:** Built multi-panel visual charts using Matplotlib (bar charts, pie charts, and subplots) to display dataset trends.---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib

---

## 📂 Project Structure

```text
nppdtraining/
├── data/
│   ├── vgchartz-2024.csv      # Raw dataset (64K rows, 15 cols)
│   └── cleanedcsv.csv         # Processed dataset with overral, year, id
├── sources/
│   ├── clean_data.py          # ETL: validation, derived features, export
│   ├── analytics.py           # Core analytics: groupby, ranking, stats, scoring
│   └── visualizatio.py        # Matplotlib visualizations (bar, pie, multi-subplot)
├── requirement.txt            # Pinned dependencies
├── .gitignore
── README.md


```

Here is the formatted Markdown ready for you to copy:

```markdown
## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed along with the required libraries:

```bash
pip install pandas numpy matplotlib

```

### 2. Execution Flow

* **Clean Data:** Validate raw sales data and produce clean CSV.(the dataset is quite cleaned, so this step just mainly validating sales)
```bash
python clean_data.py

```


* **Run Analytics:** Calculate overall metrics and print statistical summaries to the console.
```bash
python analytics.py

```


* **Generate Visualizations:** Display graphical distributions and comparison panels.
```bash
python visualization.py

```



---

## 📊 Sample Insights & Key Outputs

* **Regional Market Share:** Analyzes sales trends across NA, JP, PAL, and other regions.
* **Top Developers Analysis:** Evaluates publisher/developer output based on total volume and combined quality scores.
* **Weighted Ranking System:** Ranks games objectively using the custom normalized formula:

$$\text{Overall Score} = 0.6 \times \left(\frac{\text{Sales}}{\text{Max Sales}}\right) + 0.4 \times \left(\frac{\text{Critic Score}}{\text{Max Critic Score}}\right)$$

---

## 🔮 Future Enhancements (Roadmap)

* [ ] Implement ML Regression models (e.g., Random Forest, XGBoost) to predict global sales.
* [ ] Add K-Means Clustering to group games based on popularity and score profile.
* [ ] Build an interactive Streamlit web dashboard.

```

```
