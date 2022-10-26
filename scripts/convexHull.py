from functools import cmp_to_key
import numpy as np
class Node:
  def __init__(self, x, y, label=None):
    self.x = x
    self.y = y
    self.label = label

# essa função calcula o nó mais embaixo e, em caso de desempate, o mais a esquerda
def calculateMinimumYCoord(nodes):
    minimumNode = nodes[0]
    for node in nodes[1:]:
        if (minimumNode.y > node.y):
            minimumNode = node
        elif (minimumNode.y == node.y):
          minimumNode = node if (minimumNode.x > node.x) else minimumNode
    return minimumNode


# calcula o produto vetorial p1 x p2 em relação a p0
def crossProduct(p0, p1, p2):
    return (p1.x - p0.x)*(p2.y - p0.y) - (p2.x - p0.x)*(p1.y - p0.y)


TURNS_LEFT = 1
TURNS_RIGHT = -1
# retorna 1 se p0-p1 é anti-horario em relacao a p0-p2. caso sejam colineares, retorna 1 se p0-p1 > p0-p2
def compareVectors(p1, p2):
    cp = crossProduct(p0,p1,p2)
    if cp > 0:  
      return TURNS_RIGHT
    elif cp < 0:
      return TURNS_LEFT
    elif cp == 0:
      if calculateDistance(p0,p1) > calculateDistance(p0,p2):
          return TURNS_LEFT
      else:
          return TURNS_RIGHT

# calcula a distancia euclidiana entre dois pontos
def calculateDistance(p0,p1):
    return np.sqrt((p1.x - p0.x)**2 + (p1.y - p0.y)**2);

# imprime os nós
def printNodes(nodes):
    for node in nodes:
      print(node.x, node.y)

# algoritmo graham's scan para envoltória convexa
def convexHull(nodes):
    nodes = orderByPolarAngle(nodes)
    if (len(nodes) < 3):
      print('Convex Hull does not exist')
    grahamStack = []
    for i in range(3):
        grahamStack.append(nodes[i])
    for i in range(3, len(nodes)):
        while (1):
            if(crossProduct(grahamStack[-2], nodes[i], grahamStack[-1]) >= 0):
                grahamStack.pop()
            else:
                break

        grahamStack.append(nodes[i])
    return grahamStack

# ordena por angulo polar utilizando orientação relativa por produto vetorial
def orderByPolarAngle(nodes):
    orderedNodes = nodes.copy()
    orderedNodes.remove(p0)
    sortedNodes = sorted(orderedNodes, key=cmp_to_key(compareVectors))
    sortedNodes = [p0] +  sortedNodes
    return sortedNodes