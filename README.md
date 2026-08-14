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
── README.md                  # This file
