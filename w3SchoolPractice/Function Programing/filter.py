cities = [
    ("New York", 8500000),
    ("Los Angeles", 4000000),
    ("Chicago", 2700000),
    ("Houston", 2300000),
    ("Phoenix", 1600000),
    ("Philadelphia", 1500000),
    ("San Antonio", 1500000),
]

print("list of city and population:")
print(cities)
def has_population_greater_than_two_million(city_population):
    return city_population[1] > 2000000

million_plus_cities = list(filter(has_population_greater_than_two_million, cities))

print("\nExtract cities with a population greater than 2 million:")
print(million_plus_cities)
