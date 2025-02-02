def ping(self, url):
    import os
    os.system("ping " + url)

def download(self, url):
    import urllib.request
    response = urllib.request.urlopen(url)
    response = response.read()
    self.variables["response"] = response

def http_post(self, url, data):
    import requests
    response = requests.post(url, json = data)             
    self.variables["response"] = response
