import pika ,json,uuid

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

def PublishAndGet(project_id):
    # Declare a callback queue for receiving the response
    result = channel.queue_declare(queue='', exclusive=True)
    callback_queue = result.method.queue

    # Variable to hold the response
    response = None

    # Function to handle response
    def on_response(ch, method, props, body):
        nonlocal response
        response = body

    # Set up a consumer on the callback queue to receive the response
    channel.basic_consume(queue=callback_queue, on_message_callback=on_response, auto_ack=True)

    # Publish the project ID
    channel.basic_publish(
        exchange='',
        routing_key='admin',
        properties=pika.BasicProperties(
            reply_to=callback_queue,
            content_type='project_id'
        ),
        body=json.dumps({'id': project_id})
    )

    # Wait for the response
    while response is None:
        connection.process_data_events()

    # Return the response
    return json.loads(response)


    