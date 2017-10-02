#recommend.py
#
#Felipe Ferreira
#
#9/26/17

import sys

def simrating(user, otheruser):
    sumofnumerator = 0.0
    sumdenominatorL = 0.0
    sumdenominatorR = 0.0
    for band in range(0, len(user)):
        if(user[band]!= None and otheruser[band] != None):
            print(user[band])
            print(otheruser[band])
            numerator = user[band] * otheruser[band]
            sumofnumerator += numerator
        if(user[band] != None):
            denominatorL = user[band] **2
            sumdenominatorL += denominatorL
        if(otheruser[band] != None):
            denominatorR = otheruser[band] **2
            sumdenominatorR += denominatorR
    sumdenominator = (sumdenominatorL**(1/2)) * (sumdenominatorR**(1/2))
    simrating = sumofnumerator / sumdenominator
    return simrating

def findsmallest(mostsim, user, dict2):
    smallest = mostsim[0]
    for x in range(1,4):
        if(simrating(user,dict2[mostsim[x]]) < simrating(user, dict2[smallest])):
            smallest = mostsim[x]
    return smallest

def get3mostsimilar(user, dict2):
    mostsim = []
    mostsimf = []
    for otheruser in dict2:
        if(simrating(user,dict2[otheruser]) != 0.0 and len(mostsim) < 4):
            mostsim.append(otheruser)
        elif(simrating(user,dict2[otheruser]) != 0.0 and len(mostsim) == 4):
            for item in mostsim:
                smallest = findsmallest(mostsim, user, dict2)
                if(simrating(dict2[item],dict2[otheruser]) < simrating(user,dict2[otheruser]) and otheruser not in mostsim):
                    mostsim.remove(smallest)
                    mostsim.append(otheruser)
    for y in range(0,3):
        mostsimf.append(mostsim[y])
    return mostsimf

def option1(dict1, dict2):
    for user in dict1.keys():
        count = 0
        mostsim = get3mostsimilar(dict1[user], dict2)
        for band in dict1[user]:
            prediction = 0.0
            counter = 0
            if(band == None):
                for otheruser in mostsim:
                    bandlist = dict2[otheruser]
                    if(bandlist[count] != None):
                        prediction += bandlist[count]
                        counter += 1
                if(counter != 0):
                    prediction = prediction/counter
                else:
                    prediction = 0.0
                bandlist1 = dict1[user]
                bandlist1[count] = prediction
            count += 1
        dict1[user] = bandlist1
    return dict1

def option2(dict1, dict2):
    sumofsimratings = 0.0
    math = 0.0
    for user in dict1.keys():
        bandcount = 0
        bandlist = dict1[user]
        for band in dict1[user]:
            if(band == None):
                for otheruser in dict2.keys():
                    otherbandlist = dict2[otheruser]
                    if(otherbandlist[bandcount] != None):
                        sumofsimratings += simrating(user, otheruser)
                        math += simrating(user, otheruser) * otherbandlist[bandcount]
                replaceval = math/sumofsimratings
                bandlist[bandcount - 1] = replaceval
                dict1[user] = replaceval
                bandcount += 1
    return dict1
                
def getallbands(filename1,filename2,allband):
    forRecs = []
    file1 = open(filename1, encoding = "utf-8", mode = "r")
    labels = file1.readline()
    labels = labels.replace("\n", "")
    label = labels.split(",")
    for line in file1:
        line = line.replace("\n", "")
        instance = line.split(",")
        forRecs.append(instance)

    otherUsers = []
    file2 = open(filename2, encoding = "utf-8", mode = "r")
    labels = file2.readline()
    labels = labels.replace("\n", "")
    label = labels.split(",")
    for line in file2:
        line = line.replace("\n", "")
        instance = line.split(",")
        otherUsers.append(instance)

    for allbands in forRecs:
        if not allbands[1] in allband:
            allband.append(allbands[1])
    for allbands in otherUsers:
        if not allbands[1] in allband:
            allband.append(allbands[1])
    allband.sort()
    return allband

def main():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    otherUser = {}
    forRec = {}
    allband = []

    #creates list of all bands
    allband = getallbands(filename1, filename2, allband)
    #print(allband)
    
    #creates dictionary forRec
    file1 = open(filename1, encoding = "utf-8", mode = "r")
    file1.readline()
    for line in file1:
        labels = line.replace("\n", "")
        label = labels.split(",")
        if label[0] not in forRec.keys():
            nobands = []
            for x in range(0, len(allband)):
                nobands.append(None)
        forRec[label[0]] = nobands
        values = forRec.get(label[0])
        index = allband.index(label[1])
        values[index] = int(label[2])
            
    #creates dictionary otherUser
    file2 = open(filename2, encoding = "utf-8", mode = "r")
    file2.readline()
    for line in file2:
        labels = line.replace("\n", "")
        label = labels.split(",")
        if label[0] not in otherUser.keys():
            nobands = []
            for x in range(0, len(allband)):
                nobands.append(None)
        otherUser[label[0]] = nobands
        values = otherUser.get(label[0])
        index = allband.index(label[1])
        values[index] = int(label[2])

    option1dict = forRec
    option1dict = option1(option1dict,otherUser)
    option2dict = forRec
    #option2dict = option2(option2dict, otherUser)
    option3dict = forRec
    print(option1dict)
    #option3dict = option3(option3dict, otherUser)

    

main()
