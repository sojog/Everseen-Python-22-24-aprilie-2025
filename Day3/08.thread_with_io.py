import time
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    response = requests.get(url)
    return f"{url} -> {response.status_code}"

def sum_of_squares(n):
    return sum(i*i for i in range(n))

if __name__ == "__main__":
    urls  = [ "https://httpbin.org/delay/2" ] * 5 
    start = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_url, urls))
    
    stop = time.time()
    print("Results", results)
    print(f"Threaded  pool time  {stop-start:.2f} seconds")