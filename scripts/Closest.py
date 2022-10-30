import numpy as np
from convexHull import Node
from scipy import spatial

#Using kd-trees, realizes querys to find the closest points from two
#convexH ulls.
def ClosestPoints(chA, chB):
  chA_x = np.array([])
  chA_y = np.array([])
  
  #np array to consult closest points A in B
  arrayChA = np.empty((0,2), float)

  #Building A kd-tree
  for point in chA:
      chA_x = np.append(chA_x, point.x)
      chA_y = np.append(chA_y, point.y)
      arrayChA = np.append(arrayChA, np.array([[point.x, point.y]]), axis = 0)
  kdTreeA = spatial.KDTree(np.c_[chA_x.ravel(), chA_y.ravel()])

      
  chB_x = np.array([])
  chB_y = np.array([])

  #np array to consult closest points B in A
  arrayChB = np.empty((0,2), float)

  #Building B kd-tree
  for point in chB:
      chB_x = np.append(chB_x, point.x)
      chB_y = np.append(chB_y, point.y)
      arrayChB = np.append(arrayChB, np.array([[point.x, point.y]]), axis = 0)
  kdTreeB = spatial.KDTree(np.c_[chB_x.ravel(), chB_y.ravel()])

  #For n points in A calculates the n closest points in B
  dist_closestOfB, i_closestOfB = kdTreeB.query(arrayChA)

  #For n points in B calculates the n closest points in A 
  dist_closestOfA, i_closestOfA= kdTreeA.query(arrayChB)

  result = "null"
  #For each pair of closest points between the hulls, returns the smaller
  for i in range(len(i_closestOfB)):
      B_index = i_closestOfB.item(i)
      if(i_closestOfA.item(B_index) == i):
          if result == "null":
              result = (dist_closestOfB.item(i), i, B_index)
          elif dist_closestOfA.item(B_index) < result[0] :
              result = (dist_closestOfB.item(i), i, B_index)
  
  indexA = result[1]
  indexB = result[2]
  return (chA[indexA], chB[indexB])