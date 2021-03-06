import math

def prob(n, p, N):
    tp = math.factorial(N) / (math.factorial(n) * math.factorial(N - n))
    return tp * (p ** n) * ((1 - p) ** (N - n))

def infoMeasure(n, p, N):
    return - math.log2(prob(n, p, N))

def sumProb(N, p, n):
    sum = 0
    for i in range(0, N ):
        sum += prob(i, p, n)
    return sum

def approxEntropy(N, p, n):
    sum = 0
    for i in range(0, N):
        sum += prob(i, p, n) * infoMeasure(i, p, n)
    return sum

if __name__ == "__main__":

  print(prob(10, 1/2, 100))
  print(infoMeasure(10, 1/2, 100))
  print(sumProb(50, 1/2, 100))
  print(approxEntropy(50, 1/2, 100))
  '''
    1.3655426387463099e-17
    56.0233032504668
    0.46020538130641064
    2.0392042963658437
  '''
