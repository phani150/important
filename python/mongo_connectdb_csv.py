#!/usr/bin/python3
import pymysql;
from pprint import pprint;
from pymongo import MongoClient # import mongo client to connect
import csv;
import sys;

#=================================================================================================
# MAIN SECTION
#=================================================================================================
if __name__ == "__main__":
    #Creating instance of mongoclient
    client=MongoClient()
    csv_dict={}
    # Creating database  
    db = client.javatpoint
    csv_dict['grade']=[]
    ## read csv file.
    with open('person.csv') as csvfile:
        csv_data = csv.DictReader(csvfile)
        for row in csv_data:
            print (row)    
            firstname = row['firstname'];
            lastname = row['lastname'];
            city = row['city'];
            skillset = row['skillset'];
            csv_dict['grade'].append({'firstname':firstname,'lastname':lastname,'city':city,'skillset':skillset})
#            ks=[dict(t) for t in set([tuple(d.items()) for d in csv_dict['grade']])]
        pprint (csv_dict['grade'])
    try:
        result=db.persons.insert_many(csv_dict['grade'])
        print (result.inserted_ids)
    except:
        print (sys.exc_info()[1])
    finally:
        ks=db.persons.find()
        for doc in ks:
            print (doc)
    

