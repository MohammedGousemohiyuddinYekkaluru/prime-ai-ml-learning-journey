# Create a Python dictionary of 3 cities and thier populations. Save it to "cities.json", then load the JSON and print each city and its population. then ask the user for a new city and its population - update this info in the json file.
import json

cities = {
    "Mumbai": 12440000,
    "Delhi": 11000000,
    "Bengaluru": 8443675
}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

with open("cities.json", "r") as f:
    data = json.load(f)

for city, population in data.items():
    print(f"{city}: {population}")

new_city = input("\nEnter a new city name: ")
new_population = int(input("Enter its population: "))

data[new_city] = new_population

with open("cities.json", "w") as f:
    json.dump(data, f, indent=4)

for city, population in data.items():
    print(f"{city}: {population}")