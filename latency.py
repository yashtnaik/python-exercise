# import requests
# import time

# def check_latency(url, timeout=5):
#     try:
#         start = time.time()
#         response = requests.get(url, timeout=timeout, verify=False)
#         latency = (time.time() - start) * 1000
#         return round(latency, 2), response.status_code
#     except requests.exceptions.RequestException as e:
#         return None, f"Error: {str(e)}"

# latency, status = check_latency('https://www.google.in')
# print(f"Latency: {latency} ms, Status Code: {status}")


url=input('enter the URL link:  ')
from urllib import response
import requests
import time
import logging

logging.basicConfig(filename='latc_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

timeout=5

def latency_check(url):
    try:
        start=time.time()
        logging.info('Init time %s' % start)
        request=requests.get(url, timeout=timeout, verify=False)
        latency=(time.time() - start) * 1000
        logging.debug('Latency in milliseconds %s and status code is %s' % (latency, request.status_code))
        print(f'latency: {latency} \nStatus_Code: {request.status_code}')
    except requests.exceptions.RequestException as err :
        print(err)

latency_check(url)

