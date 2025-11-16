import os
import pandas as pd

DATA_PATH = "data/readings.csv"

def append_sample(sample: dict):
    exists = os.path.exists(DATA_PATH)
    mode = "a" if exists else "w"
    header = not exists

    import csv
    with open(DATA_PATH, mode, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=sample.keys())
        if header:
            writer.writeheader()
        writer.writerow(sample)

def load_data():
    if not os.path.exists(DATA_PATH):
        return None
    return pd.read_csv(DATA_PATH)
