#!/usr/bin/python3
import argparse
from lxml import etree
from pprint import pprint
#====================================
#====================================
if __name__=='__main__':
    parser=argparse.ArgumentParser(description='XML Parser')
    parser.add_argument('-menu','--menu',dest='menu',action='store_true',default=False,help='Display all the menu items')
    cmdlineopts=parser.parse_args()
    etree=etree.parse("plant_catolog.xml")
    CATALOG={}
    ###parse the xml file
    for plant_ele in etree.xpath("//CATALOG/PLANT"):
        bcommon=plant_ele.find('COMMON').text
        bbotani=plant_ele.find('BOTANICAL').text
        bzone=plant_ele.find('ZONE').text
        blight=plant_ele.find('LIGHT').text
        bprice=plant_ele.find('PRICE').text
        bavail=plant_ele.find('AVAILABILITY').text
        bavail=plant_ele.find('COMMON').text
        CATALOG[bcommon]=[]
        CATALOG[bcommon].extend([bbotani,bzone,blight,bprice,bavail])
    pprint (CATALOG)
    
    if cmdlineopts.menu is True:
        for bt in CATALOG.keys():
            print ("Plant common:{}".format(bt))    
