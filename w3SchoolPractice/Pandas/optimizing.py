import pandas as pd 
import numpy as np  
import time  
np.random.seed(0)  
data = np.random.randint(1, 100, size=(1000000, 1))  
df = pd.DataFrame(data, columns=['Values'])  

start_time = time.time()  
sum_for_loop = 0  
for value in df['Values']: 
    sum_for_loop += value
time_for_loop = time.time() - start_time 

start_time = time.time() 
sum_method = df['Values'].sum() 
time_sum_method = time.time() - start_time

print("Sum using for loop:", sum_for_loop)
print("Time taken using for loop:", time_for_loop, "seconds")
print("Sum using sum method:", sum_method)
print("Time taken using sum method:", time_sum_method, "seconds")
