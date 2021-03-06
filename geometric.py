import math

def prob(n, p): 
  return (1-p)**(n-1)*p

def infoMeasure(n, p):
  Pr = prob(n, p)
  return - math.log2(Pr)

def sumProb(N, p):
  '''
    - N: int
      số symbol
    - p: float or int
      xác xuất mặt ngửa
    Return:
      sum: float
  '''
  sum = 0
  for i in range(1, N):
    sum += prob(i, p)
  return sum

def approxEntropy(N, p):
  '''
    - N: int
      số symbol
    - p: float or int
      xác xuất mặt ngửa
    Return:
      H: float
  '''
  H = 0
  for i in range(1, N):
    H += prob(i, p) * infoMeasure(i, p)
  return H

if __name__ == "__main__":
  print(prob(10, 1/2)) 
  print(infoMeasure(10, 1/2)) 
  print(sumProb(20, 1/2))
  print(approxEntropy(20, 1/2))
  '''
    0.0009765625
    10.0
    0.9999980926513672
    1.999959945678711
  '''
