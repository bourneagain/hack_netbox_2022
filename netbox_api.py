import pynetbox
from pprint import pprint

# Connect to running netbox instance
nb = pynetbox.api("http://172.19.249.189:8000")

# Create token for auth
token = nb.create_token("admin", "admin")


pprint(dict(token))
pprint(list(nb.dcim.devices.all()))


nb = pynetbox.api("http://172.19.249.189:8000", token=token);

# list available devices
for device in devices:
    print(device.name)

# Create a new device
