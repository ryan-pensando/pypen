import keyring
import easygui
import getpass
import json

#keyring.set_password("pensando", "admin", "Pensando0$")
print ("Init program for pypen Python Library.")
print ("This init program securly stores Pensando PSM connection details in OS keyring services ")
print ("tenant and PSM IP address are stored in clear text")
print ("---------------------------------------------------------")
psm_temp_ip = input("Enter PSM IP address, for example 10.29.75.21: = ")
psm_ip = "https://{ip}/".format(ip=psm_temp_ip)

psm_tenant = input("Enter PSM tenant, for example default:  ")
psm_admin = input("Enter PSM admin account: ")
print ("---------------------------------------------------------")
print ("")
print ("Data Entered is ")
print ("IP address = {ip}".format(ip = psm_ip))
print ("Tenant = {t}".format(t=psm_tenant))
print ("Username = {a}".format(a=psm_admin))
print ("password is a secert")
print ("---------------------------------------------------------")

if input("Is this correct y/n: " ) == "y" or "Y" or "yes" or "Yes":
    keyring.set_password('penando', psm_admin, getpass.getpass("Enter PSM Password: "))
    data = {"ip":psm_ip, "tenant":psm_tenant}
    with open('pypen_init_data.json', 'w') as outfile:
        json.dump(data, outfile)
else:
    exit()
