def euclidiana(p1,p2):
  return np.sqrt(((p1.x-p2.x)**2 )+((p1.y-p2.y)**2))

def ForcaBruta(N, tam):
  min_val = float('inf')
  for i in range(tam):
    for j in range(i+1,tam):
      dist = euclidiana(N[i],N[j])
      if (dist < min_val):
        min_val = dist
        closest_1 = N[i]
        closest_2 = N[j]
  
  return min_val, closest_1,closest_2

def ClosestStrip(strip,tam,d):
  min_val = d
  for i in range(tam):
    j = i + 1
    while j< tam and ((strip[j].y - strip[i].y) < min_val):
      min_val = euclidiana(strip[i], strip[j])
      closest_1 = strip[i]
      closest_2 = strip[j]
      j += 1
  
  return min_val, closest_1,closest_2

def Closest(N, N_copy, tam):
  if tam <= 3:
    return ForcaBruta(N,tam)
  
  meio = tam//2
  PontoMedio = N[meio]

  N_l = N[:meio]
  N_r = N[meio:]

  d_l, aux, aux2 = Closest(N_l, N_copy, meio)
  d_r, aux3, aux4 = Closest(N_r, N_copy, tam - meio)

  d = min(d_l,d_r)

  stripN = []
  stripN_c = []
  lr = N_l + N_r
  for i in range(tam):
    if abs(lr[i].x - PontoMedio.x) < d:
      stripN.append(lr[i])
    if abs(N_copy[i].x - PontoMedio.x) < d:
      stripN_c.append(N_copy[i])
  
  stripN.sort(key = lambda point: point.y)
  d_N, close1,close2 = ClosestStrip(stripN, len(stripN), d)
  d_N_copy, close3,close4 = ClosestStrip(stripN_c, len(stripN_c), d)
                          

  min_a = min(d, d_N) 
  min_b = min(d, d_N_copy)
  if(min_a < min_b):
    return min_a, close1,close2
  else:
    return min_b, close3,close4

def ClosestPoints(N, tam):
  N.sort(key = lambda point: point.x)
  N_copy = copy.deepcopy(N)
  N_copy.sort(key = lambda point: point.y)

  return Closest(N, N_copy, len(N))