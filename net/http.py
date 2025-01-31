def ping(url):
    import os
    os.system("ping " + url)

def download(url):
    import requests
    response = requests.get(url)
    print(response.content)
