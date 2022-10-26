import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
sys.path.append(("%s/scripts")%(ROOT))

from convexHull import *
from convexHullIntersect import convexHullIntersect
import Closest

#Generates input from a file using Node class. Returns 3 sets of points, points to generate the
#covex Hulls and the set of evaluation points.
def genInput(file):

    nodesA = []
    nodesB = []
    with open('%s/inputs/%s.dat'%(ROOT, file)) as f:
        for line in f:
            if line.startswith("@attribute Class"):
                l = line.split("{")
                #Extract one label of the dataset
                labelP = l[1].split()

            if(not line.startswith("@")):
                splited = line.split(",")
                x = float(splited[0])
                y = float(splited[1])
                label = splited[-1]
                node = Node(x, y)
                if label == labelP:
                    node.label = 1
                    nodesA.append(node)
                else:
                    node.label = -1
                    nodesB.append(node)

    subsetA = []
    subsetB = []
    sizA = int(len(nodesA) * 0.7)
    sizB = int(len(nodesB) * 0.7)

    #Pick 70% of the values to be the trainning set
    subsetA = nodesA[:sizA]
    subsetB = nodesB[:sizB]

    #Pick 30% of the values to be the trainning set    
    nodesA = nodesA[sizA:]
    nodesB = nodesB[sizB:]
    evalPoints = nodesA + nodesB

    return subsetA, subsetB, evalPoints


if __name__ == '__main__': 

    #A menu to select the models that will be runned
    all = ['appendicitis', 'banana', 'bupa', 'haberman', 'magic', 
            'monk-2', 'phoneme', 'pima','saheart', 'titanic']
    
    selected = []
    btn = -2
    display = ['1.appendicitis', '2.banana', '3.bupa', '4.haberman', '5.magic', '6.monk-2',
                '7.phoneme', '8.pima','9.saheart', '10.titanic', '11.run all']
                
    while(btn != -1):
        print("Select the inputs:\n")
        for item in display:
            if item != "":
                print(("%s\t")%item)
        print("0. START")
        btn = int(input())
        btn = btn - 1
        if(btn >= 0):
            if(display[btn] == "1.appendicitis"):
                display[btn] = ""
                selected.append("appendicitis")

            elif(display[btn] == "2.banana"):
                display[btn] = ""
                selected.append("banana")
                
            elif(display[btn] == "3.bupa"):
                display[btn] = ""
                selected.append("bupa")

            elif(display[btn] == "4.haberman"):
                display[btn] = ""
                selected.append("haberman")

            elif(display[btn] == "5.magic"):
                display[btn] = ""
                selected.append("magic")

            elif(display[btn] == "6.monk-2"):
                display[btn] = ""
                selected.append("monk-2")

            elif(display[btn] == "7.phoneme"):
                display[btn] = ""
                selected.append("phoneme")

            elif(display[btn] == "8.pima"):
                display[btn] = ""
                selected.append("pima")

            elif(display[btn] == "9.saheart"):
                display[btn] = ""
                selected.append("saheart")

            elif(display[btn] == "10.titanic"):
                display[btn] = ""
                selected.append("titanic")

            elif(display[btn] == "11.run all"):
                display[btn] = ""
                selected = all
                btn = -1

    for input in selected:
        nodesA, nodesB, evalPoints = genInput(input)
