import requests


token = "AQAAAABYTSUWAADLW3qPZXyEs02zqT1NDcOfHfs"
headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }

link = 'https://cloud-api.yandex.net/v1/disk/resources'
path = 'NewPackage'
print(requests.put(f"{link}?path={path}",headers=headers))
# print(requests.get(f"{link}?path={path}",headers=headers))
