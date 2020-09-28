def get_web_call(url, session):
    try:
        api_ref = session.get(url)

    except requests.exceptions.Timeout:
        print('Network Timeout')

    except requests.exceptions.TooManyRedirects:
        print('too Many Redirects')

    except requests.exceptions.RequestException as err:
        print('Something went wrong')

        raise SystemExit(err)

    return api_ref

def post_web_call(url, session, data):

    try:
        api_ref = session.post(url, data)

    except requests.exceptions.Timeout:
        print('Network Timeout')

    except requests.exceptions.TooManyRedirects:
        print('too Many Redirects')

    except requests.exceptions.RequestException as err:
        print('Something went wrong')

        raise SystemExit(err)

    return api_ref

"""
template 
def get_x(psm_ip, session):
    
    url = psm_ip + ''
    return get_web_call(url, session).json()


"""

def get_psm_workloads(psm_ip, session):

    url = psm_ip + 'configs/workload/v1/workloads'
    return get_web_call(url, session).json()

def get_psm_cluster(psm_ip, session):

    url = psm_ip +'configs/cluster/v1/cluster'
    return get_web_call(url, session).json()

def get_flow_export_policy(psm_ip, session):

    url = psm_ip + 'configs/monitoring/v1/flowExportPolicy'
    return get_web_call(url, session).json()

def get_dsc(psm_ip, session):

    url = psm_ip + '/configs/cluster/v1/distributedservicecards'
    dsc = get_web_call(url, session).json()

    # pull out mac address of DSCs
    num_dsc = (dsc['list-meta']['total-count'])
    dsc_list = []

    for dscs in range(num_dsc):
        dsc_list.append((dsc['items'][dscs]['meta']['name']))
    return dsc, dsc_list

def get_config_snapshot(psm_ip, session):
    url = psm_ip + '/configs/cluster/v1/config-snapshot'
    return get_web_call(url, session).json()

def get_node1(psm_ip, session):
    url = psm_ip + '/configs/cluster/v1/nodes/node1'
    return get_web_call(url, session).json()

def get_alertpolices(psm_ip, session):
    url = psm_ip + '/configs/monitoring/v1/watch/tenant/default/alertPolicies'
    return get_web_call(url, session).json()

def get_networksecuritypolicy(psm_ip, session):
    url = psm_ip + '/configs/security/v1/tenant/default/networksecuritypolicies'
    return get_web_call(url, session).json()

def get_users(psm_ip, session):
    url = psm_ip + '/configs/auth/v1/tenant/default/users'
    return get_web_call(url, session).json()

def get_images(psm_ip, session):
    url = psm_ip + '/objstore/v1/tenant/default/images/objects'
    return get_web_call(url, session).json()

def get_metrics(psm_ip, session, interface):
    return None

def get_fw_logs(psm_ip, session, psm_tenant, interface, st, et):
    connector = '_'
    extension = '.csv.gzip'

    #generate the log first
    url1 = '{psm}objstore/v1/tenant/{tenant}/fwlogs/objects?field-selector=' \
        'start-time={start},end-time={end},dsc-id={int},vrf-name={tenant}'.format \
        (psm=psm_ip, int=interface, tenant=psm_tenant, start=st, end=et)
    t = get_web_call(url1, session)


    #pull the download link from the log generation response
    link = str(t.json()['items'][0]['meta']['name'])
    formatLink = link.replace("/", "_")

    #craft download url and download the data
    url = '{psm}objstore/v1/downloads/tenant/default/fwlogs/{link}'.format(psm=psm_ip, link=formatLink)

    w = get_web_call(url, session)

    return w.content







