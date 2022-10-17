#Return a bool value to indicate whether two convex holes intersects
def convex_hole_intersect(cvxHl_a, cvxHl_b):

    #List to allocate all line segments
    segments = []

    for i in range(len(cvxHl_a)):
        if(i < len(cvxHl_a) - 1):
            segments.append((cvxHl_a[i], cvxHl_a[i+1]))
        else:
            segments.append((cvxHl_a[i], cvxHl_a[0]))
    
    for i in range(len(cvxHl_b)):
        if(i < len(cvxHl_b) - 1):
            segments.append((cvxHl_b[i], cvxHl_b[i+1]))
        else:
            segments.append((cvxHl_b[i], cvxHl_b[0]))
    

#Return a bool value to indicate whether two line segments intersects
def segments_intersect(pa0, pa1, pb0, pb1):

    d1 = (pb1.x - pb0.x) * (pa0.y - pb0.y) - (pa0.x - pb0.x) - (pb1.x - pb0.x)
    d2 = (pb1.x - pb0.x) * (pa1.y - pb0.y) - (pa1.x - pb0.x) - (pb1.x - pb0.x)
    d3 = (pa1.x - pa0.x) * (pb0.y - pa0.y) - (pb0.x - pa0.x) - (pa1.x - pa0.x)
    d4 = (pa1.x - pa0.x) * (pb0.y - pa0.y) - (pb0.x - pa0.x) - (pa1.x - pa0.x)

    if( ((d1>0 and d2<0 ) or (d1<0 and d2>0)) and ((d3>0 and d4<0) or (d3<0 and d4>0)) ):
        return 1
    
    elif(d1 == 0 and on_segment(pa0, pb0, pb1)):
        return 1
    elif(d1 == 0 and on_segment(pa1, pb0, pb1)):
        return 1
    elif(d1 == 0 and on_segment(pb0, pa0, pa1)):
        return 1
    elif(d1 == 0 and on_segment(pb1, pa0, pa1)):
        return 1
    
    else:
        return 0

#Return a bool value to indicate whether a point p is in a segment i0i1
def on_segment(p, i0, i1):
    min_x = min(i0.x , i1.x)
    max_x = max(i0.x , i1.x)
    min_y = min(i0.y , i1.y)
    max_y = max(i0.y , i1.y)

    if(p.x >= min_x and p.x <= max_x and p.y >= min_y and p.y <= max_y):
        return 1
    else: 
        return 0


