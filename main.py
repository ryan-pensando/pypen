import pen, pen_auth, pen_quickstart, pen_fw_2_kafka, utils, datetime
from io import BytesIO

from time import gmtime, strftime

#PSM Vars - Set before use
PSM_IP = 'https://10.29.75.21/'
PSM_USERNAME = 'admin'
PSM_PASSWD = 'Pensando0$'
PSM_TENANT = 'default'


# Do this first or no worky worky
session = pen_auth.psm_login(PSM_IP, PSM_USERNAME, PSM_PASSWD, PSM_TENANT)
#report time
now = (datetime.datetime.utcnow()) - datetime.timedelta(minutes=15) #report size

t5 = (datetime.datetime.utcnow()) - datetime.timedelta(minutes=10) #report size

startTime, endTime = utils.return_time(now, t5)


# Get PSM workloads example
#print(pen.get_psm_workloads(PSM_IP, session))

# Get PSM cluster example
#print(pen.get_psm_cluster(PSM_IP, session))


#iterate over dict example
#cluster_name = pen.get_psm_cluster(PSM_IP, session)


# for key, value in cluster_name.items():
#     print(key, value)
#
# get name of cluster or another value from key
# print('The name of the cluster is: {0} '.format(cluster_name['meta']['name']))

#get a list of dsc, dsc = is json output, dsc_list = list of DSC
dsc, dsc_list = pen.get_dsc(PSM_IP, session)

#send fw logs to kafka
pen_fw_2_kafka.fw_kfk(PSM_IP, session, PSM_TENANT, dsc_list, startTime, endTime)

#print(pen_quickstart.quickstart_create_flow_export_policy(PSM_IP, session))

#create tenant
#print(pen_post.create_tenant(PSM_IP, session, "tischer"))
#get flow export policy
#print(pen.get_flow_export_policy(PSM_IP, session))