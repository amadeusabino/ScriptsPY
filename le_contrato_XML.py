from xml.etree import ElementTree

sourceXML = ('<RECOM><ROW><Data_Processamento>17/02/2016</Data_Processamento><LEGADO Id="1" Operador="1" /><CHAVE Origem="NETSMS-NET" Destino="NETSMS-SPREAD" /><REGISTRO Nome="TOTAL_CONTRATOS" Valor="1" Tipo="NUMERICO" /></ROW></RECOM>')
#sourceXML = ('<?xml version="1.0"?><membership><users><user nome="john" /><user nome="charles" /><user nome="peter" /><user nome="Amadeu" /><user nome="Luiz" /></users><groups><group nome="users"><user nome="john" /><user nome="charles" /></group><group nome="administrators"><user nome="peter" /></group></groups></membership>')

coluna = []
valor = []

# pega o o string e faz o parse
document = ElementTree.XML(sourceXML)

iter = document.getiterator()
#Iterate
for element in iter:
    #First the element tag name
    tag = element.tag
    #print "Element Tag:", tag
    if tag=='Data_Processamento':
        #print element.text
        coluna.append(tag)
        valor.append(element.text)
    
    #Next the attributes (available on the instance itself using
    #the Python dictionary protocol
    if element.keys():
        #print "\tAttributes:"
        for name, value in element.items():
            #print "\t\tName: '%s', Value: '%s'"%(name, value)
            coluna.append(name)
            valor.append(value)
            
print coluna
print valor           
