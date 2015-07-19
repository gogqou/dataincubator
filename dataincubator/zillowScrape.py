'''
Created on Jul 18, 2015


@author: gogqou


get SF rent prices from Zillow
import the zpids
then for each zpid get html info from webpage

'''
import numpy as np
import requests
import json

def read_zpids(first_URL):
    zpids = {}
    r = requests.get(first_URL)
    result = r.json()
    totalpages = result['list']['numPages']
    currentPage = 0
    while currentPage < 21:
        pageResult, currentPage = parseWebPage(currentPage + 1)
        print currentPage
        buildings= pageResult['map']['buildings']
    return zpids
def parseWebPage(pageNum):
    URL = 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=000010&lt=000000&ht=011000&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&days=any&ds=all&pmf=0&pf=0&zoom=10&rect=-122675056,37525792,-121920433,37863199&p={pageNumber}&sort=days&search=maplist&disp=1&listright=true&isMapSearch=1&zoom=10'.format(pageNumber = pageNum)
    r = requests.get(URL)
    pageResult =  r.json()
    currentPage =  pageResult['list']['page']
    return pageResult, currentPage
def rentAnalysis():
    
    first_page_URL = 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=000010&lt=000000&ht=011000&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&days=any&ds=all&pmf=0&pf=0&zoom=10&rect=-122675056,37525792,-121920433,37863199&p=1&sort=days&search=maplist&disp=1&listright=true&isMapSearch=1&zoom=10'
    
    zpids_dict = read_zpids(first_page_URL)
    
    
    
    #print full_requests
    #buildings= full_requests['map']['buildings']
    #for building in buildings:
        #print building
    #print full_requests.keys()
    return 1
if __name__ == '__main__':
    rentAnalysis()