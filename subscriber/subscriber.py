
import pika
import smtplib

def callback(ch, method, properties, body):
  print('Mensaje recibido:', body)

  # Procesar el mensaje (por ejemplo, extraer datos)
  datos = body.decode('utf-8')

  # Enviar correo electrónico con los datos del mensaje
  mensaje_correo = f'Asunto: Mensaje recibido\n\n{datos}'

  # Reemplazar con su dirección de correo electrónico y contraseña
  with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login('su_correo@gmail.com', 'su_contrasena')
    smtp.sendmail('su_correo@gmail.com', 'destinatario@correo.com', mensaje_correo)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='mensajes')
channel.basic_consume(callback, queue='mensajes', auto_ack=True)

print('Esperando mensajes...')

channel.start_consuming()
