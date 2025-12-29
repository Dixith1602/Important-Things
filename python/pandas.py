#finding null values with different files which are in same location/path

import pandas as pd
import numpy as np
import glob
import os

path = "/Users/Dikshu/Desktop/Python/Pandas/"
files = glob.glob(os.path.join(path, "*.csv"))

def basic_details(path):
    files = glob.glob(os.path.join(path, "*.csv"))  # Use path parameter
    results = []
    
    for file in files:
        df = pd.read_csv(file, low_memory=False)
        count_null = df.isna().sum()
        null_cols = count_null[count_null > 0]  # Only show columns with nulls
        
        print(f"\n=== {os.path.basename(file)} ===")
        print(f"Shape: {df.shape}")
        print("Null counts:")
        print(null_cols)
        print("-" * 50)
        
        # Store for return
        results.append({os.path.basename(file): null_cols.to_dict()})
    
    return results

# Usage
summary = basic_details(path)

