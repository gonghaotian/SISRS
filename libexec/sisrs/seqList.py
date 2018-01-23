#!/usr/bin/env python2
import os
import sys
##############

def createPosList(path,assembler):
    printList = open(path+'/'+assembler+'output/contigs_LocList','w')
    siteCount=0
    idx=0
    with open(path+"/"+assembler+"output/contigs_SeqLength.tsv","r") as filein:
        for line in iter(filein):
            siteCount+=idx
            splitline=line.split()
            lengthList=range(1,(int(splitline[1])+1))
            for idx,x in enumerate(lengthList):
                print>>printList,splitline[0] +'/'+str(x)
    printList.close()
    sys.stdout.write("Site list created: " + str(siteCount) + " total sites\n")

######################################################

path = sys.argv[1]
assembler = sys.argv[2]
createPosList(path,assembler)
