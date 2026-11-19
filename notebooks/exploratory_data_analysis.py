"""
Exploratory Data Analysis & Statistical Modeling Script
Project: Survey on Digital Learning Tools Usage Among College Students
Author: Waghmare Ganesh Jalindar (B.Sc. Data Science)
Institution: New Arts, Commerce and Science College, Ahmednagar
Mentor: Prof. Arjana Shaikh
"""

import os
import sys
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


def load_and_preprocess_data(raw_path: str = None) -> pd.DataFrame:
    """
    Load raw survey dataset, clean string values, remove PII, and generate ordinal score mappings.
    """
    if raw_path is None:
        potential_paths = [
            os.path.join("data", "raw", "survey_data_raw.csv"),
            os.path.join("..", "data", "raw", "survey_data_raw.csv"),
            os.path.join("data", "raw", "survey_data_raw.xlsx"),
            os.path.join("..", "data", "raw", "survey_data_raw.xlsx"),
            "fieldprojectrow.xlsx",
        ]
        for p in potential_paths:
            if os.path.exists(p):
                raw_path = p
                break

    if raw_path is None or not os.path.exists(raw_path):
        raise FileNotFoundError("Raw survey dataset could not be located.")

    print(f"[1/5] Ingesting survey dataset from: {raw_path}")
    raw = pd.read_csv(raw_path) if raw_path.endswith(".csv") else pd.read_excel(raw_path)

    # Standardize column names if not already standardized
    df = raw.copy()
    df.columns = [c.strip() for c in df.columns]

    # De-identify / Drop PII
    if "name" in df.columns:
        df_analysis = df.drop(columns=["name"])
    else:
        df_analysis = df

    # Strip whitespaces across text fields
    for col in df_analysis.columns:
        if df_analysis[col].dtype == object or str(df_analysis[col].dtype) == "string":
            df_analysis[col] = df_analysis[col].astype(str).str.strip()

    # Clean academic stream tags
    if "year_of_study" in df_analysis.columns:
        df_analysis["year_of_study"] = (
            df_analysis["year_of_study"]
            .str.replace(r"\s*\(others\)", "", regex=True)
            .str.strip()
        )

    # Map Likert scales to numeric values
    freq_map = {
        "Rarely": 1,
        "Once a week": 2,
        "2-3 days a week": 3,
        "4-6 days a week": 4,
        "Daily": 5,
    }
    help_map = {
        "slightly helpful": 1,
        "Moderately helpful": 2,
        "Very helpful": 3,
        "Extremely helpful": 4,
    }
    exp_map = {
        "Very Poor": 1,
        "Poor": 2,
        "Average": 3,
        "Good": 4,
        "Excellent": 5,
    }
    acc_map = {
        "Very inaccurate": 1,
        "Moderately inaccurate": 2,
        "Neutral / Moderately accurate": 3,
        "Accurate": 4,
        "Highly accurate": 5,
    }

    df_analysis["freq_score"] = df_analysis["frequency"].map(freq_map)
    df_analysis["help_score"] = df_analysis["helpfulness"].map(help_map)
    df_analysis["acc_score"] = df_analysis["accuracy_rating"].map(acc_map)
    df_analysis["exp_score"] = df_analysis["overall_experience"].map(exp_map)

    print(f"      Verified shape: {df_analysis.shape[0]} rows x {df_analysis.shape[1]} columns")
    print(f"      Missing values: {df_analysis.isna().sum().sum()}")
    return df_analysis


def split_multi_select(series: pd.Series) -> pd.Series:
    """Unpack pipe-separated multi-select responses into an aggregated frequency Series."""
    items = []
    for val in series.dropna():
        for part in str(val).split("|"):
            p = part.strip()
            if p and p.lower() != "nan":
                items.append(p)
    return pd.Series(Counter(items)).sort_values(ascending=False)


def run_descriptive_analysis(df: pd.DataFrame):
    """Print key descriptive statistics and cross-tabulations to terminal."""
    print("\n[2/5] Running Descriptive & Empirical Analysis...")
    n_total = len(df)
    mean_age = df["age"].mean()
    tool_adoption_pct = (df["uses_tools"] == "Yes").mean() * 100
    daily_usage_pct = (df["frequency"].isin(["Daily", "4-6 days a week"])).mean() * 100
    positive_exp_pct = (df["overall_experience"].isin(["Good", "Excellent"])).mean() * 100
    high_help_pct = (df["helpfulness"].isin(["Very helpful", "Extremely helpful"])).mean() * 100

    print(f"      Sample Size (N)              : {n_total}")
    print(f"      Mean Age                     : {mean_age:.2f} years (Range: {df['age'].min()}–{df['age'].max()})")
    print(f"      Digital Tool Adoption Rate   : {tool_adoption_pct:.1f}%")
    print(f"      Daily / Near-Daily Usage Rate: {daily_usage_pct:.1f}%")
    print(f"      High Helpfulness Rating      : {high_help_pct:.1f}%")
    print(f"      Good / Excellent Experience  : {positive_exp_pct:.1f}%")

    tools_counted = split_multi_select(df["tools_used"])
    print(f"      Top 3 Digital Tools Used     : {', '.join(tools_counted.index[:3])}")

    ai_purposes = df["ai_purpose"].value_counts()
    print(f"      Top AI Use Case              : {ai_purposes.index[0]} ({ai_purposes.iloc[0]} respondents)")


def compute_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """Compute Pearson correlation matrix across numerical and ordinal survey features."""
    print("\n[3/5] Computing Pearson Correlation Matrix...")
    num_cols = ["age", "freq_score", "help_score", "acc_score", "exp_score"]
    corr = df[num_cols].corr()
    print(corr.round(3))
    print(f"      Trust (Accuracy) ↔ Experience: r = {corr.loc['acc_score', 'exp_score']:.3f} (Strong Positive)")
    print(f"      Usage Frequency  ↔ Experience: r = {corr.loc['freq_score', 'exp_score']:.3f} (Moderate Positive)")
    return corr


def export_clean_data(df: pd.DataFrame, output_path: str = None):
    """Save processed dataset to CSV."""
    if output_path is None:
        output_path = os.path.join("data", "processed", "survey_data_cleaned.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\n[4/5] Processed data saved to: {output_path}")


def main():
    print("=" * 70)
    print(" Digital Learning Tools Survey — Exploratory Data Analysis Pipeline")
    print("=" * 70)
    df = load_and_preprocess_data()
    run_descriptive_analysis(df)
    compute_correlations(df)
    export_clean_data(df)
    print("\n[5/5] EDA Pipeline completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
