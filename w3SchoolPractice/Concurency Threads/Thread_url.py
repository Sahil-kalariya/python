import threading
import requests

def  make_request(url):
    response = requests.get(url)

if __name__ == "__main__":
    urls = ["https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org"]

    threads = []
    for url  in urls:
        thread = threading.Thread(target=make_request,args=(url,))
        thread.start()
        
    for thread in threads:
        thread.join()