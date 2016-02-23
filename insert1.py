import cx_Oracle
import time
import pika

#connection_string = "user/password@testdb"
connection_string = "dataclean/dataclean2016@dataclean"
connection = cx_Oracle.Connection(connection_string)
cursor = cx_Oracle.Cursor(connection)

# Conecta fila Rabbit
connection_rabb = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# cria fila LOG de Erros
channelLog = connection_rabb.channel()
channelLog.queue_declare(queue='RECOM_CONTRATO_LOG', durable='true')

time1 = time.time()
#print 'Time1:', time1

print 'Inserindo registros...'

for num in range(0, 10):
    #print 'inserido registro: ' + str(num) 
    try :
        cursor.execute('insert /*+append*/ into py_teste (campo1, campo2, campo3) values (:v1, :v2, :v3)', {
                            'v1' : 'valor 1hjkhkhkhkhkhkhkhk',
                            'v2' : 'valor 2',
                            'v3' : 'valor 3'
                            })
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        err = str(error.code)
        #  se der erro insere no log
        channelLog.basic_publish(exchange='',
                      routing_key='RECOM_CONTRATO_LOG',
                      properties=pika.BasicProperties(delivery_mode = 2, # make message persistent
                                                    ),
                      body='Erro Oracle: '+ err)
    else:
        connection.commit()

time2 = time.time()
#print 'Time2:', time2
print 'Finalizado - Tempo gasto:', time2 - time1

connection_rabb.close()

