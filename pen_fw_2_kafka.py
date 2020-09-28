from kafka import KafkaProducer
from io import BytesIO
import pen, gzip


kafkaServer = 'kfk1:9092' #format as localhost:9092
kafkaTopic = 'sample'

def fw_kfk(PSM_IP,session,PSM_TENANT, dsc_list, startTime, endTime):
    #kafka init
    producer = KafkaProducer(bootstrap_servers=kafkaServer)
    #producer = KafkaProducer(bootstrap_servers='10.29.75.208:9092')


    #kafka init
    producer = KafkaProducer(bootstrap_servers=kafkaServer)
#producer = KafkaProducer(bootstrap_servers='10.29.75.208:9092')


#get the report time formated for Pensando DS

    for dsc in dsc_list:
        data = pen.get_fw_logs(PSM_IP,session,PSM_TENANT, dsc, startTime, endTime)

        zipfile = gzip.open(BytesIO(data))
        for line in zipfile.readlines():
            print(line.decode('utf-8'))
            producer.send(kafkaTopic, line)

