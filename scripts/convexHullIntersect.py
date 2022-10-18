import bisect as bs
#Return a bool value to indicate whether two convex hulls intersects
def convexHullIntersect(cvxHl_a, cvxHl_b):

    #List to allocate all points
    points = []
    #List to allocate all the segments being tested in a scan pass
    segments = []

    #For each point p in both covex hulls, add a tuple in the form:
        #p[0] = point itself
        #p[1] = 1 if it is a left endpoint of a segment. 0 if it is a right endpoint.
        #p[2] = the segment which the point is related to
    for i in range(len(cvxHl_a)):
        if(i < len(cvxHl_a) - 1):
            seg = (cvxHl_a[i], cvxHl_a[i+1])
            left = min(cvxHl_a[i], cvxHl_a[i+1], key = lambda p : p.x)
            right = max(cvxHl_a[i], cvxHl_a[i+1], key = lambda p : p.x)
            points.append((left, 0, seg))
            points.append((right, 1, seg))
        else:
            seg = (cvxHl_a[i], cvxHl_a[0])
            left = min(cvxHl_a[i], cvxHl_a[0], key = lambda p : p.x)
            right = max(cvxHl_a[i], cvxHl_a[0], key = lambda p : p.x)
            points.append((left, 0, seg))
            points.append((right, 1, seg))
 
    for i in range(len(cvxHl_b)):
        if(i < len(cvxHl_b) - 1):
            seg = (cvxHl_b[i], cvxHl_b[i+1])
            left = min(cvxHl_b[i], cvxHl_b[i+1], key = lambda p : p.x)
            right = max(cvxHl_b[i], cvxHl_b[i+1], key = lambda p : p.x)
            points.append((left, 0, seg))
            points.append((right, 1, seg))
        else:
            seg =  (cvxHl_b[i], cvxHl_b[0])
            left = min(cvxHl_b[i], cvxHl_b[0], key = lambda p : p.x)
            right = max(cvxHl_b[i], cvxHl_b[0], key = lambda p : p.x)
            points.append((left, 0, seg))
            points.append((right, 1, seg))

    #Sort the points from left to right
    points.sort(key = lambda tup : (tup[0].x, tup[1], tup[0].y))

    #Realize the scan of the points and tests if the segments intersects
    for point in points:
        seg = point[2]
        keys = [r[0].y for r in segments]
        i = bs.bisect_left(keys, seg[0].y)

        if point[1] == 0:
            if(len(segments)==0):
                segments.append(seg)
            else:
                segments.insert(i, seg)
                if(i > 0 and segments[i-1][0].label != segments[i][0].label):
                    if(segmentsIntersect(segments[i-1], segments[i]) == True):
                        return True

                if(i < (len(segments) - 1) and segments[i+1][0].label != segments[i][0].label):
                    if(segmentsIntersect(segments[i], segments[i+1]) == True):
                        return True
        
        else:
            if(i > 0 and i < (len(segments) - 1) and segments[i-1][0].label != segments[i + 1][0].label):
                if(segmentsIntersect(segments[i-1], segments[i+1]) == True):
                    return True
                else:
                    segments.pop(i)

    return False
    
    
#Return a bool value to indicate whether two line segments intersects
def segmentsIntersect(segA, segB):
    pa0 = segA[0]
    pa1 = segA[1]
    pb0 = segB[0]
    pb1 = segB[1]
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