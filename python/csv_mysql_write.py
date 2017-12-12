#!/usr/bin/python3
import pymysql;
from pprint import pprint;
import csv;
import sys;
 
# Function return a connection.
#==========================================================================
#Function: getConnection
#Description: This function is used to connect to the mysql server.
#Input: Nil
#Output: returns the connection object
#==========================================================================
def getConnection():
     
    # You can change the connection arguments.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='phani123',                             
                                 db='lotuic',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
#=================================================================================================
# MAIN SECTION
#=================================================================================================
if __name__ == "__main__":
  conn = getConnection();
  persion_dict = {};
  csv_dict =[] ;
  ks=[]
  new_list=[]
  cursor=conn.cursor()
  cursor.execute('select * from persons')
  for row in cursor:
    persion_dict={'firstname':row['firstname'],'lastname':row['lastname'],'city':row['city'],'skillset':row['skillset'],'salary':row['salary']}
    ks.append(persion_dict)
  new_list=[dict(y) for y in set(tuple(x.items()) for x in ks)]   
  print (new_list)

  ## read csv file.
  with open('person.csv') as csvfile:
    csv_data = csv.DictReader(csvfile)
#   print (type(csv_data))
    count = 1;
    for row in csv_data:
#      print ("Row_data:",row) 
      firstname = row['firstname'];
      lastname = row['lastname'];
      city = row['city'];
      skillset = row['skillset'];
      salary = row['salary'];
      csv_dict.append({'firstname':firstname,'lastname':lastname,'city':city,'skillset':skillset,'salary':salary})
       
  pprint(csv_dict);

  ##
  try:
    cursor = conn.cursor();
    ##write to mysql db.
    for r in csv_dict:
      fn = r['firstname'];
      ln = r['lastname'];
      cy = r['city'];
      ss = r['skillset'];
      sy = r['salary'];
      query = "insert into persons (firstname,lastname,city,skillset,salary) values('%s','%s','%s','%s','%s')" %(fn,ln,cy,ss,sy)
      print (query)
      cursor.execute(query)
    conn.commit();
  except:
    ##roll back.
    conn.rollback();
    print(sys.exc_info()[1]);
  finally:
    # Close connection.
    conn.close();

  #pprint(persion_dict);
  
