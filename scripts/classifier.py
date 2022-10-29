import numpy as np
from convexHull import Node

#Returns the midpoint between p0 and p1
def midPoint(p0, p1):
    mp = Node((p0.x+p1.x)/2,(p0.y+p1.y)/2)
    return mp

def Reta(p1,p2):
  if(p1.x == p2.x):
    p1.x += 0.00005
  if(p1.y == p2.y):
    p1.y += 0.00005
  x = np.linspace(p1.x,p2.x)
  m = (p1.y-p2.y)/(p1.x-p2.x)
  c = p1.y - (m*p1.x)
  y = m*x + c
  return m, y

def RetaPerpendicular(pm,m):
  m_inv = -1/m
  c = pm.y -(m_inv*pm.x)
  return m_inv,c

#Classifies a new point from an equation and a point p that is above the classifier line
def classifier(equation, newNode, p):
    a, b = equation
    y = a*newNode.x + b

    if(newNode.y > y):
      return p.label
    else:
      return p.label * -1


#Calculate precision, recall and f1-score by a list of evaluation points and the classifier.
#Returns a list l[] with two lines, the first is related to the Class 1 and second related to 2.
#Both lines are triples in the form l[][0] =  precision, l[][1] = recall and l[][2] =  f1score.
def calculateMetrics(equation, points, p1):
  result = []
  totalA = 0
  totalB = 0
  matchA = 0
  matchB = 0
  falseA = 0
  falseB = 0
  for point in points:
    pLabel = point.label
    calcLabel = classifier(equation, point, p1)
    if(pLabel == 1):
      totalA = totalA + 1
      if(pLabel == calcLabel):
        matchA = matchA + 1
      else:
        falseB = falseB + 1
    else:
      totalB = totalB + 1
      if(pLabel == calcLabel):
        matchB = matchB + 1
      else:
        falseA = falseA + 1

  precisionA = matchA/(matchA + falseA)
  recallA = matchA/(matchA + falseB)
  f1ScoreA = 2*precisionA*recallA / precisionA + recallA
  result.append((precisionA, recallA, f1ScoreA))

  precisionB = matchB/(matchB + falseB)
  recallB = matchB/(matchB + falseA)
  f1ScoreB = 2*precisionB*recallB / precisionB + recallB
  result.append((precisionB, recallB, f1ScoreB))

  return result