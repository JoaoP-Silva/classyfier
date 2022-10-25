import bisect as bs
from sortedcontainers import SortedList

#Class segment that alocates two nodes and overloads the operators ">", "<" and "==" 
#accord to the coordenate y of the left endpoint of the segment.
class Segment:
    
    def __init__(self, nodeA, nodeB):
        self.nodeA = nodeA
        self.nodeB = nodeB
    
    def __gt__(sef, other):
        if(self.nodeA.y > other.nodeA.y):
            return True
        else:
            return False
    
    def __lt__(self, other):
        if(self.nodeA.y < other.nodeA.y):
            return True
        else:
            return False
    
    def __eq__(self, other):
        if(self.nodeA.y == other.nodeA.y):
            return True
        else:
            return False


#Return a bool value to indicate whether two convex hulls intersects
def convexHullIntersect(cvxHl_a, cvxHl_b):

    #List to allocate all points
    points = []
    #sortedList to allocate all the segments being tested in a scan pass
    #Accord to documentation, sortedList is implemented as a  bintree, and the
    #complexity time to add an item to list is O(log(n)).
    segments = SortedList()

    #For each point p in both covex hulls, add a tuple in the form:
        #p[0] = point itself
        #p[1] = 1 if it is a left endpoint of a segment. 0 if it is a right endpoint.
        #p[2] = the segment which the point is related to
    for i in range(len(cvxHl_a)):
        if(i < len(cvxHl_a) - 1):
            seg = Segment(cvxHl_a[i], cvxHl_a[i+1])
            left = min(cvxHl_a[i], cvxHl_a[i+1], key = lambda p : p.x)
            right = max(cvxHl_a[i], cvxHl_a[i+1], key = lambda p : p.x)
            points.append((left, 0, seg))
            points.append((right, 1, seg))
        else:
            seg = Segment(cvxHl_a[i], cvxHl_a[0])
            left = min(cvxHl_a[i], cvxHl_a[0], key = lambda p : p.x)
            right = max(cvxHl_a[i], cvxHl_a[0], key = lambda p : p.x)
            points.append((left, 0, seg))
            points.append((right, 1, seg))
 
    for i in range(len(cvxHl_b)):
        if(i < len(cvxHl_b) - 1):
            seg = Segment(cvxHl_b[i], cvxHl_b[i+1])
            left = min(cvxHl_b[i], cvxHl_b[i+1], key = lambda p : p.x)
            right = max(cvxHl_b[i], cvxHl_b[i+1], key = lambda p : p.x)
            points.append((left, 0, seg))
            points.append((right, 1, seg))
        else:
            seg =  Segment(cvxHl_b[i], cvxHl_b[0])
            left = min(cvxHl_b[i], cvxHl_b[0], key = lambda p : p.x)
            right = max(cvxHl_b[i], cvxHl_b[0], key = lambda p : p.x)
            points.append((left, 0, seg))
            points.append((right, 1, seg))

    #Sort the points from left to right
    points.sort(key = lambda tup : (tup[0].x, tup[1], tup[0].y))

    #Realize the scan of the points and tests if the segments intersects
    for point in points:
        seg = point[2]
        #keys = [r[0].y for r in segments]
        i = bs.bisect_left(segments, seg)

        if point[1] == 0:
            if(len(segments)==0):
                segments.add(seg)
            else:
                segments.add(seg)
                if(i > 0 and segments[i-1].nodeA.label != segments[i].nodeA.label):
                    if(segmentsIntersect(segments[i-1], segments[i]) == True):
                        return True

                if(i < (len(segments) - 1) and segments[i+1].nodeA.label != segments[i].nodeA.label):
                    if(segmentsIntersect(segments[i], segments[i+1]) == True):
                        return True
        
        else:
            if(i > 0 and i < (len(segments) - 1) and segments[i-1].nodeA.label != segments[i + 1].nodeA.label):
                if(segmentsIntersect(segments[i-1], segments[i+1]) == True):
                    return True
                else:
                    segments.pop(i)

    return False
    
    
#Return a bool value to indicate whether two line segments intersects.
#Expect a Segment() type object input.
def segmentsIntersect(segA, segB):
    pa0 = segA.nodeA
    pa1 = segA.nodeB
    pb0 = segB.nodeA
    pb1 = segB.nodeB
    d1 = (pb1.x - pb0.x) * (pa0.y - pb0.y) - (pa0.x - pb0.x) * (pb1.y - pb0.y)
    d2 = (pb1.x - pb0.x) * (pa1.y - pb0.y) - (pa1.x - pb0.x) * (pb1.y - pb0.y)
    d3 = (pa1.x - pa0.x) * (pb0.y - pa0.y) - (pb0.x - pa0.x) * (pa1.y - pa0.y)
    d4 = (pa1.x - pa0.x) * (pb1.y - pa0.y) - (pb1.x - pa0.x) * (pa1.y - pa0.y)

    if( ((d1>0 and d2<0 ) or (d1<0 and d2>0)) and ((d3>0 and d4<0) or (d3<0 and d4>0)) ):
        return True
    
    elif(d1 == 0 and onSegment(pa0, pb0, pb1)):
        return True
    elif(d2 == 0 and onSegment(pa1, pb0, pb1)):
        return True
    elif(d3 == 0 and onSegment(pb0, pa0, pa1)):
        return True
    elif(d4 == 0 and onSegment(pb1, pa0, pa1)):
        return True
    
    else:
        return False

#Return a bool value to indicate whether a point p is in a segment i0i1
def onSegment(p, i0, i1):
    min_x = min(i0.x , i1.x)
    max_x = max(i0.x , i1.x)
    min_y = min(i0.y , i1.y)
    max_y = max(i0.y , i1.y)

    if(p.x >= min_x and p.x <= max_x and p.y >= min_y and p.y <= max_y):
        return True
    else: 
        return False