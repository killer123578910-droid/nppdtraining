# 🎮 Video Game Sales Analysis & Machine Learning

A small end-to-end data project for analyzing video game sales data and experimenting with introductory machine learning.

This project was built as a learning project while getting familiar with **data processing, exploratory data analysis, visualization, and basic machine learning**. The main goal is not to build a production-level prediction system, but to understand how a dataset can be taken from raw data to a simple trained ML model.

## 📌 Project Overview

The project uses video game sales data to explore questions such as:

* Which genres have the highest total sales?
* Which regions contribute the most to sales?
* How do sales change over time?
* Which developers have strong sales and overall scores?
* Which games have high critic scores, sales, and overall scores?
* Can basic game information and critic scores be used to classify games into different sales-performance groups?

The project then uses a **Random Forest Classifier** to experiment with predicting a game's sales-performance class.

The project is intentionally kept at an introductory level. The focus is on understanding the workflow rather than claiming state-of-the-art ML performance.

## 🔗 Demo

A simple Streamlit application is available here:

**[Streamlit Demo](https://nppdtraining-zlk9vyycfs5aveh93vgpxb.streamlit.app/)**

The application provides an interactive way to explore the analysis and use the trained model.

## 🧠 What I Learned

This project was mainly created to practice the fundamentals of a typical data/ML workflow:

```text
Raw Dataset
    ↓
Data Cleaning
    ↓
Data Analysis
    ↓
Feature Engineering
    ↓
Label Creation
    ↓
Train / Validation Split
    ↓
Random Forest Classifier
    ↓
Evaluation
    ↓
Saved Model
    ↓
Streamlit Application
```

The repository contains separate folders for data, analysis, ML preprocessing/training, and saved models.

---

## 📊 1. Data Processing

The original dataset is stored in:

```text
data/vgchartz-2024.csv
```

The cleaning stage removes columns that are not needed for the analysis, such as `img` and `publisher`.

It also checks the relationship between:

```text
na_sales
jp_sales
pal_sales
other_sales
```

and `total_sales`.

The cleaned dataset is then saved as:

```text
data/cleanedcsv.csv
```

This part is intentionally simple because the main purpose was to become familiar with working with tabular data using **Pandas** and **NumPy**.

---

## 📈 2. Data Analysis

The analysis focuses mainly on sales, critic scores, genres, developers, regions, and release years.

Some of the analysis functions include:

* Total sales by year
* Top-selling genres
* Top developers
* Regional sales
* Highest critic-scored games
* Highest overall-scored games
* Basic statistics of total sales

For example, the project calculates:

```text
Mean sales
Maximum sales
Minimum sales
Median sales
```

It also aggregates sales by genre and region to find the largest contributors.

### Overall Score

An `overall` score is created from the dataset using a simple ranking-based formula involving:

* `total_sales`
* `critic_score`
* whether the game was updated recently

The current weighting is:

```text
50% → sales rank
40% → critic score rank
10% → recent update bonus
```

This score is mainly used as an exploratory metric for the project rather than a standardized industry rating.

---

## 📉 3. Data Visualization

The project uses **Matplotlib** to visualize several aspects of the dataset.

Examples include:

* Sales by year
* Top-selling genres
* Top developers
* Regional sales distribution
* Top games based on critic score, sales, and overall score

The visualization code is located in:

```text
sources/visualizatio.py
```

The purpose of these charts is to make patterns in the dataset easier to inspect before moving into the ML stage.

---

# 🤖 4. Machine Learning

The ML part of the project is an introductory classification experiment.

## Problem Definition

Instead of trying to directly predict the exact number of copies sold, the project converts `total_sales` into two classes based on the **75th percentile**.

Conceptually:

```text
total_sales < 75th percentile
        ↓
Class 0

total_sales >= 75th percentile
        ↓
Class 1
```

The classes represent a simplified distinction between games with relatively lower and higher sales performance.

This is a project-specific label, not an official industry classification.

---

## 🧩 Feature Engineering

Several features are created before training the model.

### Developer

Developer names are transformed into numerical values based on their historical average `overall` score.

A smoothing technique is also used to reduce the effect of developers with very few games.

### Console

Console categories are mapped using their average `overall` score.

### Genre

Genre categories are similarly mapped using their average `overall` score.

### Critic Score

Missing critic scores are replaced using the mean critic score.

Two additional features are created:

```text
critic_tier
critic_power
```

`critic_tier` divides critic scores into several ranges, while `critic_power` applies a simple nonlinear transformation to the critic score.

The final feature set is:

```text
devs_encoded
console_encoded
genre_encoded
critic_tier
critic_power
```

The implementation can be found in `ml/fitting.py`.

---

# 🌲 5. Random Forest Classifier

The main ML model is:

```text
RandomForestClassifier
```

The final training configuration currently used in the project is:

```text
n_estimators = 150
max_depth = 20
max_leaf_nodes = 300
max_features = 3
random_state = 99
```

The dataset is split into:

```text
80% → Training
20% → Validation
```

The model is then evaluated using classification accuracy.

I also experimented with `GridSearchCV` to explore different values for:

```text
n_estimators
max_depth
max_leaf_nodes
```

with 5-fold cross-validation.

However, the final script uses a fixed configuration instead of running the grid search every time, mainly to keep training faster.

---

## ⚠️ Limitations

There are several limitations to this project.

### 1. The dataset is not a perfect representation of the game industry

The analysis depends entirely on the available dataset and its existing measurements.

### 2. The target label is project-specific

The classification target is generated from the 75th percentile of `total_sales`.

Therefore:

> "Class 1" does not mean that a game is objectively successful in the real world.

It only means that the game belongs to the higher-sales group according to this dataset and threshold.

### 3. The feature engineering is relatively simple

The categorical features are converted using target/statistical information rather than a more advanced encoding pipeline.

This was done primarily as a learning exercise.

### 4. The model is not production-ready

There is no claim that this model should be used for real-world game sales forecasting.

The main purpose is to practice the basic ML workflow:

```text
data
→ preprocessing
→ features
→ labels
→ training
→ validation
→ prediction
```

### 5. Evaluation is limited

The current project mainly looks at accuracy on the validation set.

A future version could investigate additional metrics such as:

* Precision
* Recall
* F1-score
* Confusion matrix
* Cross-validation
* Feature importance

---

# 📁 Project Structure

```text
nppdtraining/
│
├── data/
│   ├── vgchartz-2024.csv
│   ├── cleanedcsv.csv
│   └── labeled_games.csv
│
├── ml/
│   ├── pre_processing.py
│   ├── fitting.py
│   └── test.py
│
├── model/
│   ├── mymodel.pkl
│   ├── le_console.pkl
│   └── le_genre.pkl
│
├── sources/
│   ├── clean_data.py
│   ├── analytics.py
│   └── visualizatio.py
│
├── requirements.txt
└── README.md
```

The repository is currently organized into separate data, analysis, ML, and model components.

---

# 🛠️ Technologies

The project mainly uses:

* **Python**
* **Pandas** — data processing and analysis
* **NumPy** — numerical operations
* **Matplotlib** — visualization
* **Scikit-learn** — machine learning
* **Joblib** — saving/loading the trained model
* **Streamlit** — interactive web application

---

# ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/killer123578910-droid/nppdtraining.git
cd nppdtraining
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

The main stages can then be explored through the scripts in:

```text
sources/
ml/
```

The trained model is stored in:

```text
model/mymodel.pkl
```
the web i set up with streamlit:
```text
https://nppdtraining-zlk9vyycfs5aveh93vgpxb.streamlit.app/
```

# 🎯 Why I Made This Project

I am currently a student learning the fundamentals of **data processing and introductory machine learning**.

This project is one of my attempts to understand the complete process of working with a dataset rather than only learning individual Python or ML concepts.

I started with relatively basic tasks:

```text
cleaning data
↓
calculating statistics
↓
grouping data
↓
creating visualizations
↓
engineering features
↓
training a simple ML model
```

There are still many things I don't know and many parts of this project that could be improved.

That is intentional.

The project represents where I am currently in my learning process rather than trying to present the project as a production-level AI system.

My longer-term goal is to become an **AI Engineer**, so I am using projects like this to gradually build a stronger foundation in:

* Data Analysis
* Machine Learning
* Python
* Model Evaluation
* Data Processing
* Deployment

---

---

# 📚 Project Status

**Status: Learning / Experimental**

This is a personal learning project.

It should be viewed as an exercise in **data analysis and introductory machine learning**, not as a production-ready game analytics or prediction system.

The main result I wanted from this project was not a perfect model, but a better understanding of the workflow from **raw data → analysis → features → ML model → application**.
