def ping(variables, url):
    import os
    os.system("ping " + url)

def download(variables, url):
    import urllib.request
    response = urllib.request.urlopen(url)
    response = response.read()
    variables["response"] = response
