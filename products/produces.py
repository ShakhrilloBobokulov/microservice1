# amqps://oopuenxw:fy8UvInD0rQkRTF-QyvDSFvPHfbBUuLg@shrimp.rmq.cloudamqp.com/oopuenxw
import pika, json

params = pika.URLParameters('amqps://oopuenxw:fy8UvInD0rQkRTF-QyvDSFvPHfbBUuLg@shrimp.rmq.cloudamqp.com/oopuenxw')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key="main", body=json.dumps(body), properties=properties)