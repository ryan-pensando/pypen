# Copyright (c) 2020, Pensando Systems
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# Author: Ryan Tischer ryan@pensando.io

import pen, pen_auth, pen_quickstart, pen_2_kafka, utils
import datetime

#PSM Vars - Set before use
PSM_IP = 'https://10.29.75.21/'
PSM_USERNAME = 'admin'
PSM_PASSWD = 'Pensando0$'
PSM_TENANT = 'default'


session = pen_auth.psm_login(PSM_IP, PSM_USERNAME, PSM_PASSWD, PSM_TENANT)
#session is used to authenicate future API calls to PSM.

#report time
now = (datetime.datetime.utcnow()) - datetime.timedelta(minutes=15)
nowDelta = (datetime.datetime.utcnow()) - datetime.timedelta(minutes=10)
#The delta of now and t5 is the size of the report.   Now must alls be before nowDelta

startTime, endTime = utils.return_time(now, nowDelta)
#get PSM formatted report time

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
#pen_fw_2_kafka.fw_kfk(PSM_IP, session, PSM_TENANT, dsc_list, startTime, endTime)


#get PSM metric
psmMetrics = pen.get_psm_metrics(PSM_IP, session, PSM_TENANT, startTime, endTime)
pen_2_kafka.send_2_kfk(psmMetrics)


#Get DSC metrics and send to Kafka
for int in dsc_list:
    data = pen.get_dsc_metrics(PSM_IP, session, PSM_TENANT, int, startTime, endTime)
    pen_2_kafka.send_2_kfk(data)

#Get DSC uplink metrics and send to Kafka
uplinkMetrics = pen.get_uplink_metrics(PSM_IP, session, PSM_TENANT, startTime, endTime)
pen_2_kafka.send_2_kfk(uplinkMetrics)

pfMetrics = pen.get_pf_metrics(PSM_IP, session, PSM_TENANT, startTime, endTime)
pen_2_kafka.send_2_kfk(uplinkMetrics)


clusterMetrics = pen.get_cluster_metrics(PSM_IP, session, PSM_TENANT, startTime, endTime)
pen_2_kafka.send_2_kfk(uplinkMetrics)

psmAlerts =  (pen.get_alerts(PSM_IP, session, PSM_TENANT))
pen_2_kafka.send_2_kfk(psmAlerts)

#pen_2_kafka.dsc_metrics_kfk(PSM_IP, session, PSM_TENANT, dsc_list, startTime, endTime)

#configure PSM based on Pensando published quickstart
#print(pen_quickstart.quickstart_create_flow_export_policy(PSM_IP, session))

#create tenant
#print(pen_post.create_tenant(PSM_IP, session, "tischer"))
#get flow export policy
#print(pen.get_flow_export_policy(PSM_IP, session))