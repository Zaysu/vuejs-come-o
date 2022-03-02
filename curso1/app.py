import requests

proxies = {
    'https' : '175.137.95.159:8080',
    'http' : '175.137.95.159:8080'
}

url = 'http://httpbin.org/ip'

req = requests.get(url, proxies = proxies)

print(req.text)