import json
from urllib.request import urlopen

url = "https://www.gov.uk/bank-holidays.json"

with urlopen(url) as response:
    data = json.load(response)

# Holidays elsewhere:
other_uk_titles = set()

for holiday in data["england-and-wales"]["events"]:
    other_uk_titles.add(holiday["title"])

for holiday in data["scotland"]["events"]:
    other_uk_titles.add(holiday["title"])

# Holidays in NI only:
print("Bank holidays unique to Northern Ireland:")
print("-" * 40)

for holiday in data["northern-ireland"]["events"]:
    if holiday["title"] not in other_uk_titles:
        print(f"{holiday['date']} - {holiday['title']}")