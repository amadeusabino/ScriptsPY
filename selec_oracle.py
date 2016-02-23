import cx_Oracle
con = cx_Oracle.connect('dataclean/dataclean2016@dataclean')

cur = con.cursor()

cur.execute('select * from dc_cidade_base')
for result in cur:
    print result

cur.close()
con.close()