import pandas as pd
import os

REQUIRED_COLUMNS = {"name", "age", "salary"}

def load_data(data):
    return pd.read_csv(data)

def validate_columns(df):
    cols = set(df.columns.str.lower())
    if not REQUIRED_COLUMNS.issubset(cols):
        raise ValueError(f"Faltan columnas requeridas: {REQUIRED_COLUMNS - cols}")

def average_salary(df):
    return df['salary'].mean()

def people_of_30(df):
    return df[df['age'] > 30]

def save_to_csv(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)