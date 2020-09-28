import requests
import json

#get rid of insecure warnings -
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def psm_login (psm_ip, username, password, tenant):

    auth_data = {
        "username": username,
        "password": password,
        "tenant": tenant
    }
    data_to_send = json.dumps(auth_data).encode("utf-8")

    #Create session for PSM

    session = requests.Session()
    session.verify = False

    #working
    URL = psm_ip + 'v1/login'

    auth = session.post(URL, data_to_send)

    return session