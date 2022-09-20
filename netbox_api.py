import pynetbox
nb = pynetbox.api("http://172.19.249.189:8000")
token = nb.create_token("admin", "admin")
from pprint import pprint
pprint(dict(token))
pprint(list(nb.dcim.devices.all()))
nb = pynetbox.api("http://172.19.249.189:8000", token=token);
for device in devices:
    print(device.name)

