'''
Created on Jul 18, 2015


@author: gogqou


get SF rent prices from Zillow
import the zpids
then for each zpid get html info from webpage

'''
import numpy as np
import requests
import bs4
class Listing(object):
    def __init__(self, ListingID):
        self.ID = ListingID
    
def getListingLinks(first_URL):
    linksList = []
    r = requests.get(first_URL)
    result = r.json()
    #totalpages = result['list']['numPages']
    currentPage = 0
    while currentPage < 2:
        pageResult, currentPage = parseWebPage(currentPage + 1)
        print currentPage
        pageSoup = bs4.BeautifulSoup(pageResult['list']['listHTML'], 'lxml')
        for link in bs4.BeautifulSoup(pageResult['list']['listHTML'], 'lxml', parse_only=bs4.SoupStrainer('a')):
            if link.has_attr('href'):
                print link['href']
                linksList.append(link['href'])
        
    return linksList
def parseWebPage(pageNum):
    URL = 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=000010&lt=000000&ht=011000&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&days=any&ds=all&pmf=0&pf=0&zoom=10&rect=-122675056,37525792,-121920433,37863199&p={pageNumber}&sort=days&search=maplist&disp=1&listright=true&isMapSearch=1&zoom=10'.format(pageNumber = pageNum)
    r = requests.get(URL)
    pageResult =  r.json()
    currentPage =  pageResult['list']['page']
    return pageResult, currentPage
def getListingAttribs(zpids):
    for key, value in zpids.iteritems():
        zpids[key]=fetchListingPage(value)
    
    return zpids
def fetchListingPage(Listing):
    listingURL = 'http://www.zillow.com/homedetails/3805-Atlantic-Brigantine-Blvd-Brigantine-NJ-08203/{listingNum}_zpid/'.format(listingNum = Listing.ID)
    listingPage = requests.get(listingURL)
    Listing.fullpageData = bs4.BeautifulSoup(listingPage.text)
    #print Listing.fullpageData.prettify()
    Listing.fullpageData.find_all()
    return Listing

def rentAnalysis():
    
    first_page_URL = 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=000010&lt=000000&ht=011000&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&days=any&ds=all&pmf=0&pf=0&zoom=10&rect=-122675056,37525792,-121920433,37863199&p=1&sort=days&search=maplist&disp=1&listright=true&isMapSearch=1&zoom=10'
    fullLinks = getListingLinks(first_page_URL)
    
    #populated_zpids = getListingAttribs(zpids)
    return 1
if __name__ == '__main__':
    rentAnalysis()