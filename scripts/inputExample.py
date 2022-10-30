from convexHull import *
from convexHullIntersect import convexHullIntersect
from classifier import *


#Generates a example input using te database 'iris.dat'.
#Returns a tuple t in the form: t[0] = 70% of data from label A; t[1] = 70% of data from label B; t[2] = Eval points
def inputExample():
    dt = open('./inputs/wine.dat')
    lines = dt.readlines()
    att = 0
    index_data = -1
    all_att = 0
    for line in lines:
        #Variable to save the line that data start
        index_data += 1
        if line.startswith("@attribute"):
            #Set the number of attributes
            att += 1
        if line.startswith("@attribute Class"):
            l = line.split("{", 1)[1]
            l = l.split("}")[0]
            #Extract one label of the dataset
            l = l.split(",")
            labelDA = l[0].strip()
            #The second is setted as the last one
            labelDB = l[-1].strip()
        if(not line.startswith("@")):
            all_att = len(line.split(","))
            break

    #Iterates over all combinations of attribute pairs in the dataset, if its linearly separable, write output and
    #goes to the next dataset. If none of them is linearly separable, write that the set is not linearly separable.
    for i in range(all_att):
        for j in range(i + 1, all_att -1):
            nodesA = []
            nodesB = []
            for l_i in range(index_data, len(lines)):
                line = lines[l_i]
                if(not line.startswith("@")):
                    splited = line.split(",")
                    x = float(splited[i])
                    y = float(splited[j])
                    label = splited[-1].strip()
                    node = Node(x, y)
                    if(label == labelDA):
                        node.label = 1
                        nodesA.append(node)
                    elif(label == labelDB):
                        node.label = -1
                        nodesB.append(node)
            sizA = int(len(nodesA) * 0.7)
            sizB = int(len(nodesB) * 0.7)

            #Pick 70% of the values to be the trainning set
            subset70A = nodesA[:sizA]
            subset70B = nodesB[:sizB]

            #Pick 30% of the values to be the trainning set    
            subset30A = nodesA[sizA:]
            subset30B = nodesB[sizB:]
            evalPoints = subset30A + subset30B

            vanNodesA = subset70A
            vanNodesB = subset70B

            chA = convexHull(subset70A)
            chB = convexHull(subset70B)
            if(not convexHullIntersect(chA, chB)):
                return vanNodesA, vanNodesB, evalPoints
    
    print('Error')
    return -1

