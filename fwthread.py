#!/usr/bin/python

import urllib
import threading
      
      
domain = '?????.appspot.com'
    
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
  
def push(asset):
    url = 'http://%s/%s?name=%s' %(domain, asset.get('uuid'), asset.get('name'))
    r = urllib.urlopen(url).read()
    # return the response from the app
    return r
 
def worker():
    # work down the items in the list and call the push
    # function to create the entity in the datastore 
    asset = assetlist.pop()
    r = push(asset)
    # print the response from the app
    print r
        

def main():
    for i in range(10):
        t = threading.Thread(target=worker)
        t.start()

if __name__ == "__main__":
    main()
