import math

def prob(n, p, r):
    tp = math.factorial(n - 1) / (math.factorial(n - r) * math.factorial(r - 1))
    return tp * (p ** r) * ((1 - p) ** (n - r))

def infoMeasure(n, p, r):
    return - math.log2(prob(n, p, r))

def sumProb(N, p, r):
    sum = 0
    for i in range(r, N):
        sum += prob(i, p, r)
    return sum

def approxEntropy(N, p, r):
    sum = 0
    for i in range(r, N):
        sum += prob(i, p, r) * infoMeasure(i, p, r)
    return sum

if __name__ == "__main__":
  print(prob(20, 1/2, 10))
  print(infoMeasure(20, 1/2, 10))
  print(sumProb(100, 1/2, 20))
  print(approxEntropy(100, 1/2, 20))

  '''
    0.08809852600097656
    3.5047383085276858
    0.9999999997802984
    4.680314850022563
  '''
