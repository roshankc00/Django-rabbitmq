import pika,json
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(channel,method,properties,body):
    print(body,'consumer')
    if properties.content_type=='product_created':
        message = json.loads(body)
        print(message,"consumer")
        


channel.basic_consume(queue='admin',on_message_callback=callback,auto_ack=True)


print("hahah statred")
channel.start_consuming()