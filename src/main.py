from utils import generate_monthly_end_timestamps, get_block_number_by_timestamp
from data_fetching import fetch_all_reserves_at_block, fetch_reserve_details
import json
import os

from data_processing import load_data, preprocess_data
from analysis import calculate_average_liquidity
from visualization import plot_average_liquidity_rate

def analyzeData():
    years = [2021, 2022, 2023]
    avg_liquidity_rates = []
    for year in years:
        data = load_data(year)
        df = preprocess_data(data)
        avg_rate = calculate_average_liquidity(df)
        avg_liquidity_rates.append(avg_rate)

    plot_average_liquidity_rate(years, avg_liquidity_rates)


def main(api_key):
    years = [2020]  # Extend this list to include more years if needed
    timestamps_by_year = generate_monthly_end_timestamps(years)
    
    for year, timestamps in timestamps_by_year.items():
        print(f"Fetching data for {year}...")
        block_numbers = [get_block_number_by_timestamp(ts, api_key) for ts in timestamps]
        monthly_data = []

        for month_idx, block in enumerate(block_numbers):
            print(f"Processing data for {year}, month {month_idx + 1}...")
            reserves = fetch_all_reserves_at_block(block)  # Assuming this function can accept a block number
            month_reserves_details = []

            for reserve in reserves:
                reserve_details = fetch_reserve_details(reserve['id'])
                month_reserves_details.append(reserve_details)

            monthly_data.append(month_reserves_details)
        
        # Save the detailed data monthly for the current year
        file_name = f'detailed_reserves_data_{year}.json'
        with open(file_name, 'w') as f:
            json.dump(monthly_data, f, indent=4)
        print(f"All monthly reserve details for {year} have been fetched and saved.")
    analyzeData()


if __name__ == "__main__":
    api_key = '1Y6U7AXRN322CEFFA524VXWMS5V73PYA5P'
    main(api_key)
