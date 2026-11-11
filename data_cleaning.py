"""Data cleaning for the Diabetes Health Indicators dataset (BRFSS 2015).

Input:  diabetes_012_health_indicators_BRFSS2015.csv
        (Kaggle: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
Output: clean_diabetes_v2.csv (used by analisi_diabete.R)

Usage:  python data_cleaning.py
"""
import pandas as pd

RAW_FILE = "diabetes_012_health_indicators_BRFSS2015.csv"
CLEAN_FILE = "clean_diabetes_v2.csv"

df = pd.read_csv(RAW_FILE)

# Remove duplicate records
df = df.drop_duplicates()

# Binary target: prediabetes (1) and diabetes (2) are merged into a single class
df["diabetes"] = df["Diabetes_012"].isin([1, 2]).astype(int)
df = df.drop(columns=["Diabetes_012"])

# Consistent snake_case variable names
df = df.rename(columns={
    "HighBP": "high_bp",
    "HighChol": "high_chol",
    "CholCheck": "chol_check",
    "BMI": "bmi",
    "Smoker": "smoker",
    "Stroke": "stroke",
    "HeartDiseaseorAttack": "heart_disease",
    "PhysActivity": "physical_activity",
    "Fruits": "fruits",
    "Veggies": "veggies",
    "HvyAlcoholConsump": "heavy_alcohol",
    "AnyHealthcare": "healthcare",
    "NoDocbcCost": "no_doc_cost",
    "GenHlth": "general_health",
    "MentHlth": "mental_health",
    "PhysHlth": "physical_health",
    "DiffWalk": "diff_walk",
    "Sex": "sex",
    "Age": "age",
    "Education": "education",
    "Income": "income",
})

df.to_csv(CLEAN_FILE, index=False)
print(f"Saved {len(df):,} rows x {df.shape[1]} columns to {CLEAN_FILE}")
