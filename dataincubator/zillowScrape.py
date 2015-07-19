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
    def __init__(self, ListingURL):
        self.URL = 'http://www.zillow.com'+ListingURL
####################################################################
                                                                  ##      
def getListingLinks(first_URL, addon):
    linksDict = {}
    r = requests.get(first_URL.format(addOn = addon, pagenumber = 1))
    result = r.json()
    totalpages = result['list']['numPages']
    print totalpages
    currentPage = 0
    while currentPage < totalpages and currentPage<20:
        pageResult, currentPage = parseWebPage(currentPage + 1, first_URL, addon)
        print currentPage
        pageSoup = bs4.BeautifulSoup(pageResult['list']['listHTML'], 'lxml')
        for link in bs4.BeautifulSoup(pageResult['list']['listHTML'], 'lxml', parse_only=bs4.SoupStrainer('a')):
            if link.has_attr('href') and 'myzillow' not in link['href']:
                #print link['href']
                linksDict[link['href']] = Listing(link['href'])
    print len(linksDict)
    return linksDict

def parseWebPage(pageNum, baseURL, addon):
    URL = baseURL.format(addOn = addon, pagenumber = pageNum)
    r = requests.get(URL)
    pageResult =  r.json()
    currentPage =  pageResult['list']['page']
    return pageResult, currentPage
                                                                  ##
####################################################################

####################################################################
                                                                  ##
                                                                  
def makeListtoDict (List):
    listDict = {}
    for item in List:
        listDict[item] = Listing(item) #making it a listing object with URL
    return listDict
def getListingAttribs(linksdict):
    for key, value in linksdict.iteritems():
        linksdict[key]=fetchListingPage(value)
    return linksdict
def fetchListingPage(Listing):
    
    listingPage = requests.get(Listing.URL)
    Listing.fullpageData = bs4.BeautifulSoup(listingPage.text)
    #print Listing.fullpageData.prettify()
    print Listing.fullpageData.find_all('a')
    return Listing
                                                                  ##
####################################################################

####################################################################
                                                                  ##
def getURLs(first_page_URL):
    Q1 = '13&rect=-122465930,37725821,-122377610,37786555'
    Q2 = '12&rect=-122556181,37755854,-122366667,37828293'
    Q3 = '13&rect=-122516056,37747846,-122422843,37808563'
    Q4 = '11&rect=-122490521,37780483,-122167798,38022942'
    fullLinks = getListingLinks(first_page_URL, Q1)
    fullLinks.update(getListingLinks(first_page_URL, Q2))
    fullLinks.update(getListingLinks(first_page_URL, Q3))
    fullLinks.update(getListingLinks(first_page_URL, Q4))
    return fullLinks

def write_dict_to_file(dictionary):
    with open('listingURLs.txt', 'w') as fp:
        for p in dictionary.keys():
            fp.write(p + '\n')
    '''
    with open ('wvtc_data.txt', 'w') as fp:
    for p in main_dic.items():
        fp.write("%s:%s\n" % p)
        '''
    return 1
def read_dict_from_file(filename):
    with open(filename,'r') as fp:
        fileList = [x.strip() for x in fp.readlines()] 
    return fileList
                                                                  ##
####################################################################

####################################################################
                                                                  ##
                                                                  ##                                                                  
def rentAnalysis():
    #used below once to write a txt file with listing URLs
    #after first run, just read from file for quicker access
    #first_page_URL = 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=000010&lt=000000&ht=011000&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&days=any&ds=all&pmf=0&pf=0&zoom={addOn}&p={pagenumber}&sort=days&search=maplist&disp=1&listright=true&isMapSearch=1&zoom=13' 
    #linksDict = getURLs(first_page_URL)
    #write_dict_to_file(linksDict)
    
    #read from URLs txt file to populate a dictionary of Listing objects
    listingList = read_dict_from_file ('listingURLs.txt')
    listingDict=makeListtoDict(listingList)
    populated_links = getListingAttribs(listingDict)
    return 1
if __name__ == '__main__':
    rentAnalysis()
####################################################################