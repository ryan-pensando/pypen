# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer

# Import sys module
import sys

# Define server with port
bootstrap_servers = ['kfk1:9092']

# Define topic name from where the message will recieve
topicName = 'sample'

# Initialize consumer variable
consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers =
   bootstrap_servers)

# Read and print message from consumer
while True:
    for msg in consumer:
        print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))

# Terminate the script
sys.exit()