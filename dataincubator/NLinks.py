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
def Nlinks():
    N = 8
    
    repeats = 1000
    bagList = np.linspace(1, N, N)
    print bagList
    linksList = []
    while len(bagList)>0:
        index = np.random.randint(0, len(bagList))
        linksList.append(bagList[index])
        bagList = np.delete(bagList, index)
        print linksList
        print bagList
    return 1


if __name__ == '__main__':
    Nlinks()