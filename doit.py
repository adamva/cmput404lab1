import requests
req_ver = requests.__version__
print('requests version: ' + req_ver)
g_home = requests.get('https://www.google.com')
# print(g_home)

src_code = requests.get('https://raw.githubusercontent.com/adamva/cmput404lab1/master/doit.py')
print('\n' + src_code.text)
