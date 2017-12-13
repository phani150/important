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
    etree=etree.parse("sample.xml")
    breakfast_menu={}
    ###parse the xml file
    for food_ele in etree.xpath("//breakfast_menu/food"):
        btype=food_ele.get('type')
        if breakfast_menu.get('btype') is None:
            breakfast_menu[btype]={}
        bname=food_ele.find('name').text
#        print (bname)
        bprice=food_ele.find('price').text
        bdescription=food_ele.find('description').text
        bcalories=food_ele.find('calories').text
        breakfast_menu[btype][bname]={}
        breakfast_menu[btype][bname]['price']=bprice
        breakfast_menu[btype][bname]['description']=bdescription
        breakfast_menu[btype][bname]['calories']=bcalories
    ##
    pprint (breakfast_menu)
    ##get all the menu items
    if cmdlineopts.menu is True:
        for bt in breakfast_menu.keys():
            print ("MenuType:{},".format(bt))
            for bn in breakfast_menu[bt].keys():
                print ("MenuName:{},".format(bn)) 

