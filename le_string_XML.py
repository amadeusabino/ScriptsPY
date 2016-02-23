from xml.etree import ElementTree

sourceXML = ('<?xml version="1.0"?><membership><users><user name="Bruno" /><user name="charles" /><user name="peter" /><user name="Amadeu" /><user name="Luiz" /></users><groups><group name="users"><user name="john" /><user name="charles" /></group><group name="administrators"><user name="peter" /></group></groups></membership>')

# pega o o string e faz o parse
document = ElementTree.XML(sourceXML)

users = document.find( 'users')

for user in document.findall( 'users/user' ):    
    print user.attrib[ 'name' ]
   
for group in document.findall( 'groups/group' ):
    print 'Group:', group.attrib[ 'name' ]
    print 'Users:'
    for node in group.getchildren():
        if node.tag == 'user':
            print '    -', node.attrib[ 'name' ]    