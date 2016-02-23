import pika
import cx_Oracle
from xml.etree import ElementTree

# Conecta banco e abre cursor
connection_string = "dataclean/dataclean2016@dataclean"
connection_ora = cx_Oracle.Connection(connection_string)
cursor = cx_Oracle.Cursor(connection_ora)

# Conecta fila Rabbit
connection_rabb = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection_rabb.channel()
channel.queue_declare(queue='RECOM_CONTRATO', durable='true')

# cria fila LOG de Erros
channelLog = connection_rabb.channel()
channelLog.queue_declare(queue='RECOM_CONTRATO_LOG', durable='true')

print ' **** Esperando e processando mensagens da fila Rabbit.... CTRL+C para sair.'

def callback(ch, method, properties, body):
    #print " [x] Received %r" % (body,)
    # lista valor com conteudo do XML que esta em body
    XMLParse(body)
#    print valor

#dados do XML ['Data_Processamento', 'Operador', 'Id', 'Destino', 'Origem', 'Nome', 'Tipo', 'Valor'] 
    
    try: 
        cursor.execute('insert /*+append*/ into rc_teste_xml values (:v0, :v1, :v2, :v3, :v4, :v5, :v6, :v7)', {
                            'v0' : valor[0],  #data_processamento
                            'v1' : valor[2],  #legado_id
                            'v2' : valor[1],  #legado_operador
                            'v3' : valor[4],  #chave_origem
                            'v4' : valor[3],  #chave_destino
                            'v5' : valor[5],  #registro_nome
                            'v6' : valor[7],  #registro_valor
                            'v7' : valor[6]   #registro_tipo
                            })
    except Exception:
            #  se der erro insere no log
            channelLog.basic_publish(exchange='',
                                     routing_key='RECOM_CONTRATO_LOG',
                                     properties=pika.BasicProperties(delivery_mode = 2, # make message persistent
                                                                     ),
                                     body=body)
    else: 
        connection_ora.commit()
    
def XMLParse(xml):
    # gera lista com o conteudo do XML passado
    sourceXML = xml
    global valor, coluna
    valor = []
    coluna = []
        
    # pega o o string e faz o parse
    document = ElementTree.XML(sourceXML)
    iter = document.getiterator()
    #Iterate
    for element in iter:
        #First the element tag name
        #    print "Element:", element.tag 
        tag = element.tag 
        if tag=='Data_Processamento':
            #print element.text
            coluna.append(tag)
            valor.append(element.text)
            
        #    Next the attributes (available on the instance itself using
        #the Python dictionary protocol
        if element.keys():
            #            print "\tAttributes:"
            for name, value in element.items():
                #print "\t\tName: '%s', Value: '%s'"%(name, value)
                coluna.append(name)
                valor.append(value)
    
channel.basic_consume(callback,
                      queue='RECOM_CONTRATO',
                      no_ack=True)

channel.start_consuming()