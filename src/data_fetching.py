import requests
import pandas as pd

def fetch_all_reserves_at_block(block_number=None):
    url = "https://api.thegraph.com/subgraphs/name/aave/protocol-v2"
    block_filter = f'(block: {{number: {block_number}}})' if block_number else ''
    query = f"""
    {{
        reserves{block_filter} {{
            id
            name
            liquidityRate
            variableBorrowRate
            stableBorrowRate
        }}
    }}
    """
    response = requests.post(url, json={'query': query})
    if response.status_code == 200:
        return response.json()['data']['reserves']
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")
    

def fetch_all_reserves():
    url = "https://api.thegraph.com/subgraphs/name/aave/protocol-v2"
    query = """
    {
        reserves(where: {
    usageAsCollateralEnabled: true
  }) {
            id
            name
            liquidityRate
            variableBorrowRate
            stableBorrowRate
        }
    }
    """
    response = requests.post(url, json={'query': query})
    if response.status_code == 200:
        return response.json()['data']['reserves']
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")

def fetch_reserve_details(reserve_id):
    url = "https://api.thegraph.com/subgraphs/name/aave/protocol-v2"
    detailed_query = f"""
    {{
        reserve(id: "{reserve_id}") {{
            id
            name
            liquidityRate
            variableBorrowRate
            stableBorrowRate
            price {{
                id
            }}
        }}
    }}
    """
    response = requests.post(url, json={'query': detailed_query})
    if response.status_code == 200:
        return response.json()['data']['reserve']
    else:
        raise Exception(f"Failed to fetch detailed data: {response.status_code} {response.text}")
