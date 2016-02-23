from lxml import etree
doc = etree.parse('C:/Users/t2016716/Documents/0_scriptsPY/Recom_Total_Contratos.xml')

memoryElem = doc.find('RECOM')
print memoryElem 
#print memoryElem.text        # element text
print memoryElem.get('unit') # attribute