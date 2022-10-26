def midPoint(p0, p1):
    node = Node((p0.x+p1.x)/2,(p0.y+p1.y)/2,"MIDPOINT")

def findSlope(p0,p1):
    return (p1.y - p0.y)/(p1.x - p0.x)

def findTransversalLine(slope, midPoint):
    b = slope*midPoint.x - midPoint.y
    return (1/slope, midPoint.x, b)

def classifier(equation, newNode):
    a, x, b = equation
    y = a*newNode.x + b

    if (y > newNode.y):
        return 1
    else:
        return -1
