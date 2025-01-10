from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
ladd1 = "27488 Stanford Avenue, North Dakota"
print("Location address:",ladd1)
location = geolocator.geocode(ladd1)
print("Street address, street name: ")
print(location.address)
ladd2 = "380 New York St, Redlands, CA 92373"
print("\nLocation address:",ladd2)
location = geolocator.geocode(ladd2)
print("Street address, street name: ")
print(location.address)
ladd3 = "1600 Pennsylvania Avenue NW"
print("\nLocation address:",ladd3)
location = geolocator.geocode(ladd3)
print("Street address, street name: ")
print(location.address)
