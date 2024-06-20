import json
import pandas as pd

def load_data(year):
    with open(f'./data/detailed_reserves_data_{year}.json', 'r') as file:
        data = json.load(file)
    return data

def preprocess_data(data):
    flattened_data = []
    for month_data in data:
        for reserve in month_data:
            reserve['liquidityRate'] = float(reserve['liquidityRate']) / 1e18
            reserve['variableBorrowRate'] = float(reserve['variableBorrowRate']) / 1e18
            reserve['stableBorrowRate'] = float(reserve['stableBorrowRate']) / 1e18
            flattened_data.append(reserve)
    df = pd.DataFrame(flattened_data)
    return df
