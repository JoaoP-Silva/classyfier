from convexHull import Node
import os
import sys
root = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
root = os.path.abspath(os.path.join(root, os.pardir))
ROOT_DIR = root
sys.path.insert(1, ROOT_DIR)


#Generates input from 'banana.dat' file using Node class.
def genInput():

    nodesA = []
    nodesB = []
    with open('%s/banana.dat'%(ROOT_DIR)) as f:
        for line in f:
            x, y, label = line.split(",")
            x = float(x)
            y = float(y)
            label = float(label)
            node = Node(x, y)
            if label == 1:
                node.label = 1
                nodesA.append(node)
            else:
                node.label = -1
                nodesB.append(node)

    return nodesA, nodesB