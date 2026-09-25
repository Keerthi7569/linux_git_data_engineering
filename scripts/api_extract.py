
import requests
import json
from pathlib import Path
from datatime import datatime

API_URL = "https://jsonplaceholder.typicode.com/users"

OUTPUT_DIR = Path("api_data")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "users.json"

print("Starting API data extraction...")
print(f"Extraction time: {datetime.now()}")
print(f"API URL: {API_URL}")

response = requests.get(API_URL, timeout=30)

if response.status_code == 200:
    data = response.json()

    with open(OUTPUT_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Successfully extracted {len(data)} records.")
    print(f"Data saved to: {OUTPUT_FILE}")

else:
    print(f"API request failed.")
    print(f"Status code: {response.status_code}")
