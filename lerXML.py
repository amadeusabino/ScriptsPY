from xml.etree import ElementTree

document = ElementTree.parse( 'membership.xml' )

membership = document.getroot()
users = membership.find( 'users' )

for user in document.findall( 'users/user' ):
    print user.attrib[ 'name' ]

for group in document.findall( 'groups/group' ):
    print group.attrib[ 'name' ]
    
for group in document.findall( 'groups/group' ):
    print 'Group:', group.attrib[ 'name' ]
    print 'Users:'
    for node in group.getchildren():
        if node.tag == 'user':
            print '-', node.attrib[ 'name' ]    