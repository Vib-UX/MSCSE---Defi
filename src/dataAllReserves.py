import requests
import pandas as pd

def fetch_all_reserves():
    url = "https://api.thegraph.com/subgraphs/name/aave/protocol-v2"
    reserves = []
    skip = 0
    first = 100  # Fetch 100 reserves at a time, adjust based on your needs and API limits
    continue_fetching = True

    while continue_fetching:
        query = f"""
        {{
            reserves(first: {first}, skip: {skip}) {{
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
            data = response.json()['data']['reserves']
            if data:
                reserves.extend(data)
                skip += len(data)
            else:
                continue_fetching = False
        else:
            raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")

    return reserves


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

def main():
    reserves = fetch_all_reserves()
    detailed_reserves = []

    for reserve in reserves:
        reserve_details = fetch_reserve_details(reserve['id'])
        detailed_reserves.append(reserve_details)
        print(f"Fetched details for {reserve['name']}")

    # Optionally, convert this list to a DataFrame or save it to a file
    # Here's an example of saving this data to a JSON file
    import json
    with open('detailed_reserves_data1.json', 'w') as f:
                json.dump(detailed_reserves, f, indent=4)

    print("All reserve details have been fetched and saved.")

if __name__ == "__main__":
    main()


