import requests
import time
import calendar

def generate_monthly_end_timestamps(years):
    """Generate Unix timestamps for the last moment of each month for the given years."""
    timestamps = {}
    for year in years:
        timestamps[year] = []
        for month in range(1, 13):
            last_day = calendar.monthrange(year, month)[1]
            time_str = f"{year}-{month}-{last_day} 23:59:59"
            struct_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            timestamp = calendar.timegm(struct_time)
            timestamps[year].append(timestamp)
    return timestamps

def get_block_number_by_timestamp(timestamp, api_key):
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'block',
        'action': 'getblocknobytime',
        'timestamp': str(timestamp),
        'closest': 'before',
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            return data['result']
        else:
            raise Exception(f"Etherscan API error: {data['message']}")
    else:
        raise Exception(f"API request failed with status {response.status_code}")
