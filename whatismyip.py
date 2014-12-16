#pip install requests
import requests
r = requests.get('http://whatismyip.eth1.in')
print r.content
