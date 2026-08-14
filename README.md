# 🎮 Video Game Sales Analytics & Insights Pipeline

A Python-based data processing, feature engineering, and visual analytics pipeline designed to evaluate global video game performance, regional market trends, and developer success metrics using VGChartz data.

---

## 📌 Project Overview

This project provides an automated end-to-end data pipeline that processes raw video game sales records, validates multi-regional sales statistics, engineers normalized evaluation metrics, and visualizes market trends.

### Key Highlights:
* **Data Cleaning & Validation:** Verified regional sales breakdown against total reported sales to ensure data consistency.
* **Feature Engineering:** Developed a weighted scoring algorithm (`overall`) combining normalized `total_sales` (60%) and `critic_score` (40%) to evaluate true game success.
* **Exploratory Data Analysis (EDA):** Extracted market trends by year, genre dominance, top-performing developers, and regional revenue share.
* **Data Visualization:** Built multi-panel dashboards using Matplotlib for clear visual reporting.

---

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

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed along with the required libraries:

```bash
pip install pandas numpy matplotlib

```

### 2. Execution Flow

* **Clean Data:** Validate raw sales data and produce clean CSV.


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
