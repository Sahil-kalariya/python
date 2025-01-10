import urllib3
from urllib.parse import urlparse, urlunparse

original_url = 'https://www.example.com/path/to/resource?param1=value1¶m2=value2'

parsed_url = urlparse(original_url)

parsed_url = parsed_url._replace(path='/new/path', query='new_param=new_value')

modified_url = urlunparse(parsed_url)

http = urllib3.PoolManager()

try:
    response = http.request('GET', modified_url)
    
    if response.status == 200:
        print("Request Successful!")
        print("Response:")
        print(response.data.decode('utf-8'))
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status}")

except Exception as e:
    print(f"Error: {e}")

