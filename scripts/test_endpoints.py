import urllib.request, json

url = 'http://127.0.0.1:5000/save_result'
data = json.dumps({'winner': 'TestX'}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as resp:
    print('save_result status', resp.status)
    print(resp.read().decode())

with urllib.request.urlopen('http://127.0.0.1:5000/history') as resp2:
    print('history status', resp2.status)
    print(resp2.read().decode())
