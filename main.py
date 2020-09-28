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
print(dsc_list)
#send fw logs to kafka
#pen_fw_2_kafka.fw_kfk(PSM_IP, session, PSM_TENANT, dsc_list, startTime, endTime)


#get metric
print (pen.get_psm_metrics(PSM_IP, session, PSM_TENANT, startTime, endTime))

for int in dsc_list:
    print (pen.get_dsc_metrics(PSM_IP, session, PSM_TENANT, int, startTime, endTime))

pen_fw_2_kafka.dsc_metrics_kfk(PSM_IP, session, PSM_TENANT, dsc_list, startTime, endTime)
#print(pen_quickstart.quickstart_create_flow_export_policy(PSM_IP, session))

#create tenant
#print(pen_post.create_tenant(PSM_IP, session, "tischer"))
#get flow export policy
#print(pen.get_flow_export_policy(PSM_IP, session))