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


from kafka import KafkaProducer
from io import BytesIO
import pen, gzip, json


kafkaServer = 'kfk1:9092' #format as localhost:9092
kafkaTopic = 'sample'

def fw_kfk(PSM_IP,session,PSM_TENANT, dsc_list, startTime, endTime):
    #kafka init
    producer = KafkaProducer(bootstrap_servers=kafkaServer)

    for dsc in dsc_list:
        data = pen.get_fw_logs(PSM_IP,session,PSM_TENANT, dsc, startTime, endTime)

        zipfile = gzip.open(BytesIO(data))
        for line in zipfile.readlines():
            #print(line.decode('utf-8'))
            producer.send(kafkaTopic, line)

def dsc_metrics_kfk(PSM_IP,session,PSM_TENANT, dsc_list, startTime, endTime):
    # Example - Sends DSC metrics to Kafka.  Probally easier do use send_2_kfk
    producer = KafkaProducer(bootstrap_servers=kafkaServer)
    for int in dsc_list:
        data = pen.get_dsc_metrics(PSM_IP, session, PSM_TENANT, int, startTime, endTime)
        producer.send(kafkaTopic, json.dumps(data).encode('utf-8'))

def send_2_kfk(data):
    #accepts JSON formated data to send to Kafka
    producer = KafkaProducer(bootstrap_servers=kafkaServer)
    producer.send(kafkaTopic, json.dumps(data).encode('utf-8'))
