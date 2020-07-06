import requests
from akamai.edgegrid import EdgeGridAuth,EdgeRc
from urllib.parse import urljoin
edgerc = EdgeRc('~/.edgerc')
section = 'DEFAULT'
baseurl = 'https://%s' % edgerc.get(section, 'host')
s = requests.Session()
s.auth=EdgeGridAuth.from_edgerc(edgerc, section)
def addingIP(a):
    path = '/network-list/v2/network-lists/80813_APITESTING/elements?element='
    full_path = path+a
    url = urljoin(baseurl,full_path)
    b = s.put(url)
    print(b.json())
    return b
a = str(input())
addingIP(a)
