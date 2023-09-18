# amqps://oopuenxw:fy8UvInD0rQkRTF-QyvDSFvPHfbBUuLg@shrimp.rmq.cloudamqp.com/oopuenxw
import pika

params = pika.URLParameters('amqps://oopuenxw:fy8UvInD0rQkRTF-QyvDSFvPHfbBUuLg@shrimp.rmq.cloudamqp.com/oopuenxw')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("recieved in admin")
    print(body)
    # channel.basic_publish(exchange='', routing_key='main', body="hello main"),

channel.basic_consume(queue="admin", on_message_callback=callback)
print("consumer started")
channel.start_consuming()
channel.close()