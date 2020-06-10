import requests
from akamai.edgegrid import EdgeGridAuth
from urllib.parse import urljoin
baseurl = 'https://akab-to3rfihztgdee3zk-joieup7teartdnnl.luna.akamaiapis.net'
s = requests.Session()
s.auth = EdgeGridAuth(
client_secret = 'UtFhs/R0T0OQRalr3swmxiwREiQfEQnO7u+n31rnaeI=',
access_token = 'akab-dasxt6zzpylpgkgu-5uiapf22skbytcup',
client_token = 'akab-kffyn4lxq3yb6bto-wwsb5d2ntrjt4pfd')

result = s.get(urljoin(baseurl, '/diagnostic-tools/v2/ip-addresses/49.231.112.203/mtr-data?destinationDomain=www.bangkokbank.com&resolveDns=true'))
print(result.json())
print(result.status_code)
