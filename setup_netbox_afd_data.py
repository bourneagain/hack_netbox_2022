import pynetbox
import pprint
import sys

token = "431408c934524f47092f14a5b26972ccca38d58b"
nb = pynetbox.api(url="http://172.19.249.189:8000", token=token)
def delete_devices():
    nb.dcim.devices.delete(nb.dcim.devices.all())

def delete_manufacturers():
    nb.dcim.manufacturers.delete(nb.dcim.manufacturers.all())

def delete_device_roles():
    nb.dcim.device_roles.delete(nb.dcim.device_roles.all())

def delete_device_types():
    nb.dcim.device_types.delete(nb.dcim.device_types.all())

def delete_sites():
    nb.dcim.sites.delete(nb.dcim.sites.all())

def init():
    delete_devices()
    delete_device_roles()
    delete_device_types()
    delete_manufacturers()
    delete_sites()

init()

site_list = []
device_role_list = []
device_type_list = []
manufacturer_list = []

def create_device(dev):
    result = nb.dcim.devices.create(
            name=dev,
            device_role=device_role_list[0],
            site=site_list[0],
            device_type=device_type_list[0],
            )
    print(result)

def create_sites(site):
    result = nb.dcim.sites.create(name="afd_site_1", slug="afd")
    print(result)

def list_sites():
    result = nb.dcim.sites.all()
    for site in result:
        print("Site id = %s, name = %s" % (site.id, site.name))
        site_list.append(site.id)

def list_devices():
    result = nb.dcim.devices.all()
    for device in result:
        print("device name = %s, device id = %s" % (device.name, device.id))

def create_device_role(name, slug):
    result = nb.dcim.device_roles.create(name=name, slug=slug)
    print(result)

def list_device_role():
    result = nb.dcim.device_roles.all()
    for role in result:
        print("Role id = %s, name = %s" % (role.id, role.name))
        device_role_list.append(role.id)

def create_manufacturer(name, slug):
    result = nb.dcim.manufacturers.create(name=name, slug=slug)
    print(result)

def create_device_type(manufacturer, model, slug):
    result = nb.dcim.device_types.create(manufacturer=manufacturer, model=model, slug=slug)
    print(result)

def list_device_types():
    result = nb.dcim.device_types.all()
    for man in result:
        print("device_type id = %s" % (man.id))
        device_type_list.append(man.id)

def list_manufacturers():
    result = nb.dcim.manufacturers.all()
    for man in result:
        print("Manufacturer id = %s, name = %s" % (man.id, man.name))
        manufacturer_list.append(man.id)


# create site
# This is needed before creating other objects
print("############# Creating Site...")
create_sites("afd_site1")

print("############# Listing Sites..")
list_sites()

# Create device_role
print("############# Creating device role...")
create_device_role("Afd_PF_Host", "afd_pf")


# List device roles
print("############# Listing Device roles...")
list_device_role()

# Create Manufacture
print("############# Creating Manufacturer...")
create_manufacturer("MSFT", "msft")

# list manufactures
print("############# Listing manufacturer...")
list_manufacturers()


print("############# Creating device type...")
create_device_type(manufacturer_list[0], 1, "edgevm")

print("############# Listing manufacturer...")
list_device_types()

# Create a device on the site
print("############# Creating a device: testdev")
create_device("testdev")

# List devices 
print("############# Creating a device: testdev")
list_devices()


sys.exit()
