import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    if properties.content_type == 'project_id':
        project_id = json.loads(body)['id']
        project_details = fetch_project_details(project_id)
        ch.basic_publish(
            exchange='',
            routing_key=properties.reply_to,
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id,
                content_type='application/json'
            ),
            body=json.dumps(project_details)
        )

def fetch_project_details(project_id):
    return {'id': project_id, 'name': 'Project Name', 'description': 'Project Description'}

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('message pattern listener listening ')
channel.start_consuming()
