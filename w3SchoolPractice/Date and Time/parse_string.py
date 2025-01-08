import time

time_string = "22 January, 2020"
print("String representing time:", time_string)
result = time.strptime(time_string, "%d %B, %Y")
print(result)