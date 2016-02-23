from xml.dom import minidom

xmldoc = ('<RECOM><ROW><LEGADO Id="111" Operador="3" /><CHAVE Origem="NETSMS-NET" Destino="NETSMS-SPD" /><REGISTRO Nome="TOTAL_CONTRATOS" Valor="1" Tipo="NUMERICO" /></ROW></RECOM>')
 
#minidom.parse('c:\itens.xml')
itemlist = xmldoc.getElementsByTagName()

print('numero de itens', len(itemlist))
print('item 1: ', itemlist[0].attributes['RECOM'].value)
for s in itemlist:
    print(s.attributes['RECOM'].value)
    

    