
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='mensajes')

message = '¡Hola, mundo!'
channel.basic_publish(exchange='', routing_key='mensajes', body=message)

print('Mensaje enviado a la cola')

connection.close()
