import json
import pprint
import sseclient
import codingchallenge.DatabaseConnector as dc 

def with_urllib3(url):
    """Get a streaming response for the given event feed using urllib3."""
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False)

def with_requests(url):
    """Get a streaming response for the given event feed using requests."""
    import requests
    return requests.get(url, stream=True)

url = 'http://localhost:8080/streamTest/sse'
response = with_urllib3(url)  # or with_requests(url)
client = sseclient.SSEClient(response)
for event in client.events():
    data = json.loads(event.data)
    counterparty = data["cpty"]
    instrument = data["instrumentName"]
    price = float(data["price"])
    quantity = int(data["quantity"])
    time = data["time"]
    deal_type = data["type"]
    dc.insertData5(counterparty, instrument, price, quantity, time, deal_type)
