import json
from urllib.request import urlopen

url = "https://www.gov.uk/bank-holidays.json"

with urlopen(url) as response:
    data = json.load(response)

print("Northern Ireland Bank Holidays:")
print("-" * 40)

for holiday in data["northern-ireland"]["events"]:
    print(f"{holiday['date']} - {holiday['title']}")