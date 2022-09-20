import pynetbox
from pprint import pprint

# Connect to running netbox instance
nb = pynetbox.api("http://172.19.249.189:8000")

# Create token for auth
token = nb.create_token("admin", "admin")
pprint(dict(token))

# list available devices
nb = pynetbox.api("http://172.19.249.189:8000", token=token["key"]);
devices = nb.dcim.devices.all()

for device in devices:
    print(device.name)
