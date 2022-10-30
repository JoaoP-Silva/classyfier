import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
sys.path.append(("%s/scripts")%(ROOT))

from convexHull import *
from convexHullIntersect import convexHullIntersect
from Closest import ClosestPoints
from classifier import *
    
if __name__ == '__main__': 

    #A menu to select the models that will be runned
    allData = ['balance', 'contraceptive', 'haberman', 'hayes-roth', 'heart', 'ionosphere', 'iris', 'magic',
            'monk-2', 'newthyroid', 'phoneme', 'pima', 'ring', 'sonar', 'spambase', 'thyroid', 'titanic',
            'twonorm', 'wdbc', 'wine']

    for data in allData:
        dt = open('%s/inputs/%s.dat'%(ROOT, data))
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
        flag = False
        f = open("output.txt","a")
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

                chA = convexHull(subset70A)
                chB = convexHull(subset70B)
                if(not convexHullIntersect(chA, chB)):
                    flag = True
                    #Calculate the closest points between the hulls
                    pA, pB = ClosestPoints(chA, chB)
                    mid = midPoint(pA, pB)
                    m = Reta(pA,pB)[0]
                    equation = RetaPerpendicular(mid, m)
                    #Get results and write on file
                    result = calculateMetrics(equation, evalPoints, pA)

                    precisionA = result[0][0]
                    recallA = result[0][1]
                    f1scoreA = result[0][2]
                    precisionB = result[1][0]
                    recallB = result[1][1]
                    f1scoreB = result[1][2]

                    s = (("set %s, attributes %d and %d:\n\t precisionA = %f recallA = %f f1scoreA = %f\n"%(data, i, j, precisionA, recallA, f1scoreA)))
                    f.write(s)
                    s = (("\t precisionB = %f recallB = %f f1scoreB = %f\n"%(precisionB, recallB, f1scoreB)))
                    f.write(s)
                    print(("Writed output for %s")%(data))
                    break
            else:
                continue

            break
        
        if(not flag):
            s = (("set %s is not linearly separable\n")%(data))
            f.write(s)
        

    print("End.")


