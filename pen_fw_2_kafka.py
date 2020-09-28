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
            print(line.decode('utf-8'))
            producer.send(kafkaTopic, line)

def dsc_metrics_kfk(PSM_IP,session,PSM_TENANT, dsc_list, startTime, endTime):
    # kafka init
    producer = KafkaProducer(bootstrap_servers=kafkaServer)
    for int in dsc_list:
        data = pen.get_dsc_metrics(PSM_IP, session, PSM_TENANT, int, startTime, endTime)
        producer.send(kafkaTopic, json.dumps(data).encode('utf-8'))
