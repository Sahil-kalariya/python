import time
import datetime

time_string = "22 January, 2020"
print("String representing time:", time_string)
result = time.strptime(time_string, "%d %B, %Y")
print(result)



# Print the minimum time (midnight) in the datetime module
print("First Second: ", datetime.time.min)
# Print the maximum time (11:59:59.999999) in the datetime module
print("Last Second: ", datetime.time.max)
