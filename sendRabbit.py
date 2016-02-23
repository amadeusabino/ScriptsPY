import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# cria fila
channel.queue_declare(queue='Send_PY', durable='true')

time1 = time.time()

for num in range(0, 1000000):
    channel.basic_publish(exchange='',
                      routing_key='Send_PY',
                      properties=pika.BasicProperties(delivery_mode = 2, # make message persistent
                                                    ),
                      body='Mensagem enviada via Python!')

    
print " [x] Sent 'Mensagens enviadas'"
time2 = time.time()
#print 'Time2:', time2
print 'Finalizado - Tempo gasto:', time2 - time1

connection.close()