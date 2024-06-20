
# def main():
#     reserves = fetch_all_reserves()
#     detailed_reserves = []

#     for reserve in reserves:
#         reserve_details = fetch_reserve_details(reserve['id'])
#         detailed_reserves.append(reserve_details)
#         print(f"Fetched details for {reserve['name']}")

#     # Optionally, convert this list to a DataFrame or save it to a file
#     # Here's an example of saving this data to a JSON file
#     import json
#     with open('detailed_reserves_data.json', 'w') as f:
#                 json.dump(detailed_reserves, f, indent=4)

#     print("All reserve details have been fetched and saved.")

# if __name__ == "__main__":
#     main()


