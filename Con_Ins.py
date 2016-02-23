import pika
import cx_Oracle

connection_string = "dataclean/dataclean2016@dataclean"
connection_ora = cx_Oracle.Connection(connection_string)
cursor = cx_Oracle.Cursor(connection_ora)


connection_rabb = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection_rabb.channel()

#channel.queue_declare(queue='Send_PY', durable='true')
channel.queue_declare(queue='RECOM_CONTRATO', durable='true')

print ' [*] Waiting and processing messages..... To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    cursor.execute('insert /*+append*/ into py_teste (campo1, campo2, campo3) values (:v1, :v2, :v3)', {
                            'v1' : 'valor 1',
                            'v2' : 'valor 2',
                            'v3' : 'valor 3'
                            })
    connection_ora.commit()

channel.basic_consume(callback,
                      queue='RECOM_CONTRATO',
                      no_ack=True)

channel.start_consuming()