#!/usr/bin/python3
import MySQLdb
import pymysql
from pprint import pprint
import sys
# Connect to the database
def getConnection():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='phani123',
                             db='lotuic',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection
if __name__=='__main__':
    conn=getConnection()
    persion_dict={}
    check={}
    ks=[] 
    try:
        cursor=conn.cursor()
        print (type(cursor))
        cursor.execute('select * from anandh')
        for row in cursor:
            print (type(row))
            print ("-----------------------------")
            print ('row:',row)
            print ('age:',row['age'])
            print ('location:',row['location'])
            age=row['age']
            location=row['location']
#            persionid=row['id']
            persion_dict={'age':row['age'],'location':row['location']} 
            ks.append(persion_dict)
        new_list=[dict(y) for y in set(tuple(x.items()) for x in ks)]    
#        dummy=True    
        for d in ks:
#            for (k,v) in d.keys(): 
#               print (k,v)
#                if k==d['age'] and v==d['location']:
#                    pass
#                else:
#                    dummy=False
             k=d['age']
             v=d['location']
             sql="insert into anandh(age,location) values('%d','%s')" %(k,v)
             print (sql)
             cursor.execute(sql)
    except:
        print (sys.exc_info()[1])
    finally:
        conn.close()
        print (ks)
