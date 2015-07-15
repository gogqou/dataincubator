'''
Created on Jul 15, 2015

@author: gogqou




You have a chain with N links numbered 1 through N. 
Every minute, you draw a random link from a bag, and connect it to any other consecutively-numbered link that you drew before. 
For example, if you drew 4,1,5,7,3, you would end up with three subchains: 1,(3,4,5),7. 
You keep on drawing until you have drawn all N links and connected them into a single chain of length N. 
Let M be the maximum number of subchains in this process.

'''
import numpy as np
import itertools as iter
from operator import itemgetter
import matplotlib.pyplot as plt
def group_consec(inputList):
    consecList = []
    ranges = []

    for k, g in iter.groupby(enumerate(inputList), lambda (i,x):i-x):
        group = map(itemgetter(1), g)
        ranges.append((group[0], group[-1]))
    print 'ranges', ranges
    print 'num links', len(ranges)
    return len(ranges)

def Mdistr(repeats = 2):
    N = 8
    max_links = np.zeros([repeats, 1])
    for i in range(0,repeats):
        max_links[i] = Nlinks(N)
    #calc mean
    
    #plot distribution
    
    plt.plot(max_links)
    plt.show()
    #calc standard dev
    
def Nlinks(N=8):
    M = 0
    bagList = np.linspace(1, N, N)
    print bagList
    linksList = []
    while len(bagList)>0:
        #randomly find index and move from "bag" to chain list
        index = np.random.randint(0, len(bagList))
        linksList.append(bagList[index])
        linksList.sort()
        bagList = np.delete(bagList, index)
        print linksList
        numLinks = group_consec(linksList)
        if numLinks>M:
            M = numLinks
        #order and form chains of consecutive integers in the linksList
        #itertools
        
    return M


if __name__ == '__main__':
    Mdistr()