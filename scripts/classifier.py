def midPoint(p0, p1):
    node = Node((p0.x+p1.x)/2,(p0.y+p1.y)/2,"MIDPOINT")

##def findSlope(p0,p1):
##    return (p1.y - p0.y)/(p1.x - p0.x)

##def findTransversalLine(slope, midPoint):
##    b = slope*midPoint.x - midPoint.y
##    return (1/slope, midPoint.x, b)

def Reta(p1,p2):
  x = np.linspace(p1.x,p2.x)
  m = (p1.y-p2.y)/(p1.x-p2.x)
  c = p1.y - (m*p1.x)
  y = m*x + c
  return m, y

def RetaPerpendicular(pm,m):
  m_inv = -1/m
  c = pm.y -(m_inv*pm.x)
  y = m_inv*x + c
  return m_inv,c

def classifier(equation, newNode):
    a, x, b = equation
    y = a*newNode.x + b

    if (y > newNode.y):
        return 1
    else:
        return -1
