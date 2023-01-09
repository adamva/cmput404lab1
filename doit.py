import requests
req_ver = requests.__version__
print('requests version: ' + req_ver)
g_home = requests.get('https://www.google.com')
# print(g_home)
