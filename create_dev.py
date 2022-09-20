import pynetbox
import time

dev = "R3"
token = "4ac8ed5e369eb445b02cfa422a3db26723c6ad8b"
def adddev(dev):
    nb = pynetbox.api(url="http://172.19.249.189:8000", token=token)
    result = nb.dcim.devices.create(
            name=dev,
            device_role=3,
            site=1,
            device_type=1,
            )
    print(result)

adddev("testdev")

