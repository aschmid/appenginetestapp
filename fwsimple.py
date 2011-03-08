#!/usr/bin/python

import urllib            
  
def main():
    # work down the items in the list one after each other and create the entity
    # in the big table
    assetlist = [{'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'1'}, 
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'2'},
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'3'}, 
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'4'},
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'5'}, 
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'6'},
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'7'}, 
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'8'},
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'9'},
                {'uuid':'418a88ae-496d-11e0-8638-58b035f549d3', 'name':'10'} ]
                
    domain = '?????.appspot.com'      

    for asset in assetlist:
        url = 'http://%s/%s?name=%s' %(domain, asset.get('uuid'), asset.get('name'))
        r = urllib.urlopen(url).read()
        print r
        
if __name__ == "__main__":
    main()
        