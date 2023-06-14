import ipaddress
import json
import logging

from django.conf import settings

logging.warning("azure_ip start")
with (settings.BASE_DIR / 'data' / 'ServiceTags_Public_20230529.json').open() as f:
    dat = json.load(f)

d = []
for product in dat['values']:
    for prefix in product['properties']['addressPrefixes']:
        r = ipaddress.ip_network(prefix)
        d.append((prefix, int(r.network_address), int(r.broadcast_address), product['name']))
logging.warning(len(d))
logging.warning("finished")


def lookup(addr: str) -> []:
    ans = []
    ip_int = int(ipaddress.ip_address(addr))
    for i in range(0, len(d)):
        if d[i][1] <= ip_int <= d[i][2]:
            ans.append((d[i][0], d[i][3]))
    return ans
