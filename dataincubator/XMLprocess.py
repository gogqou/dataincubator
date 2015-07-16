'''
Created on Jul 15, 2015

@author: gogqou
'''

import sys
import xml.etree.ElementTree as ET
import xml
import glob
import os
#######################################################
                                                     ##
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
def postTags (xmlTree):
    root = xmlTree.getroot()
    postCount = 0
    for row in root.findall('row'):
        postCount = postCount + 1
    
    return postCount
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
    Tagsfile = homePath +'Tags.xml'
    tagsTree = ET.parse(Tagsfile)
    Postsfile = homePath + 'Posts.xml'
    postsTree = ET.parse(Postsfile)
    ithTag= tagSorting(tagsTree)
    ithTagCount = float(ithTag[1])
    postCount = postTags(postsTree)
    print 'Fraction of posts with fifth most popular tag = ', ithTagCount/postCount
    #for child in root:
        #print(child.tag, child.attrib)
    
    return 1
                                                    ##
######################################################
if __name__ == '__main__':
    parseXML()