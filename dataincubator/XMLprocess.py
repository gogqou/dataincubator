'''
Created on Jul 15, 2015

@author: gogqou
'''

import sys
import xml.etree.ElementTree as ET
import xml
import glob
import os
########################################################
                                                     ###
def tagSorting(xmlTree):
    root = xmlTree.getroot()
    tags_counts = []
    i = 5 #  return the ith most popular tag
    for row in root.findall('row'):
        
        count = int(row.get('Count'))
        tag = row.get('TagName')
        tags_counts.append((tag, count))
    tags_counts = sorted(tags_counts, key = lambda tag:tag[1], reverse= True)
    return tags_counts[i-1]
                                                    ###
#######################################################

#######################################################
                                                     ##
def postsCount(xmlTree):
    root = xmlTree.getroot()
    postCount = 0
    for row in root.findall('row'):
        if 'Tags' in row.attrib:
            #print row.attrib 
            postCount = postCount + 1
    
    return postCount
def scoring(xmlTree):
    root = xmlTree.getroot()
    average_score = 0
    for child in root:
        print(child.tag, child.attrib)
    
    return average_score
######################################################
                                                    ##
                                                    ##                                                        
def parseXML():
    homePath = sys.argv[1]
    files = os.listdir(homePath)
    for file in files:
        if '.gz' not in file:
            filename, ext = os.path.splitext(file)
            path = homePath + file
    
    #Question 1        
    Tagsfile = homePath +'Tags.xml'
    tagsTree = ET.parse(Tagsfile)
    Postsfile = homePath + 'Posts.xml'
    postsTree = ET.parse(Postsfile)
    ithTag= tagSorting(tagsTree)
    ithTagCount = float(ithTag[1])
    postCount = postsCount(postsTree)
    print 'Fraction of posts with fifth most popular tag = ', ithTagCount/postCount

    #Question 2
    
#     Votesfile = homePath + 'Votes.xml'
#     votesTree = ET.parse(Votesfile)
    #average_score= scoring(postsTree)
    
    
    
    
    #for child in root:
        #print(child.tag, child.attrib)
    
    return 1
                                                    ##
######################################################
if __name__ == '__main__':
    parseXML()