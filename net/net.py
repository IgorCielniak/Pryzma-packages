def ping(variables, url):
    import os
    os.system("ping " + url)

def download(variables, url):
    import urllib.request
    response = urllib.request.urlopen(url)
    response = response.read()
    variables["response"] = response

def http_post(variables, url, data):
    import requests
    response = requests.post(url, json = data)             
    variables["response"] = response
