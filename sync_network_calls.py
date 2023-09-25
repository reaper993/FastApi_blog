import time
import requests

def main():
    request_count = 10
    url = "https://httpbin.org/net"
    session = requests.Session()
    for i in range(request_count):
        print(f"making request {i+1}/{request_count}")
        resp = session.get(url)
        if resp.status_code == 200:
            pass

start = time.time()
main()
end = time.time()
print(f"Total time: {end-start} seconds")
