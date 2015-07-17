'''
Created on Jul 15, 2015

@author: gogqou
'''

import sys
import xml.etree.ElementTree as ET
import xml
import glob
import os
import collections
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
#######################################################
def scoring(xmlTree):
    root = xmlTree.getroot()
    post_total_score = 0
    answer_total_score = 0
    postCount = 0
    answerCount = 0
    for row in root.findall('row'):
        if row.attrib['PostTypeId']=='1':
            post_total_score = float(row.attrib['Score'])+post_total_score
            postCount = postCount +1
        else:
            answer_total_score = float(row.attrib['Score'])+answer_total_score
            answerCount = answerCount +1
    post_average_score = float(post_total_score)/postCount
    
    answer_average_score = float(answer_total_score)/answerCount
    return post_average_score, answer_average_score
                                                    ###
#######################################################
def userRep(userxmlTree, postxmlTree):
    PearsonCorrelation=0
    userRoot = userxmlTree.getroot()
    postRoot = postxmlTree.getroot()
    userDict = collections.defaultdict(list)
    for child in userRoot:
        userDict[child.attrib['Id']].append(child.attrib['Reputation'])
        userDict[child.attrib['Id']].append(0)
    print userRoot.findall('row')[1].attrib['Id']
    for child in postRoot:
        if 'OwnerUserId' in child.attrib.keys():
            if child.attrib['OwnerUserId'] in userDict:
                #print userDict[child.attrib['OwnerUserId']]
                print 'check'
                userDict[child.attrib['OwnerUserId']][1] = userDict[child.attrib['OwnerUserId']][1] + float(child.attrib['Score'])
        
    print userDict[2]
    return PearsonCorrelation
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
#     Tagsfile = homePath +'Tags.xml'
#     tagsTree = ET.parse(Tagsfile)
    Postsfile = homePath + 'Posts.xml'
    postsTree = ET.parse(Postsfile)
#     ithTag= tagSorting(tagsTree)
#     ithTagCount = float(ithTag[1])
    #postCount = postsCount(postsTree)
    
#     print 'Fraction of posts with fifth most popular tag = ', ithTagCount/postCount

    #Question 2
    
    
    #postAvgScore, answerAvgScore= scoring(postsTree)
    #print 'Post Avg Score = ', postAvgScore, 'Answer Avg Score = ', answerAvgScore
    
    #Question 3
    Usersfile = homePath + 'Users.xml'
    userTree = ET.parse(Usersfile)
    correlationP = userRep(userTree, postsTree)
    #for child in root:
        #print(child.tag, child.attrib)
    
    return 1
                                                    ##
######################################################
if __name__ == '__main__':
    parseXML()