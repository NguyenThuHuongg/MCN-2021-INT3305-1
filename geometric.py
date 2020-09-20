# -*- coding: utf-8 -*-
"""geometric.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16fuDDAkT_oMc9ozfYhR-ZbaqULufgOoG
"""

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
  print(prob(5, 1/2)) 
  print(infoMeasure(5, 1/2)) 
  print(sumProb(50, 1/2))
  print(approxEntropy(50, 1/2))
  '''
    0.03125
    5.0
    0.9999999999999982
    1.9999999999999094
  '''