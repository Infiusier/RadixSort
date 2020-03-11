#RadixSort
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import sys
sys.setrecursionlimit(10**9)
lista=[]
tamanhos=[20000,30000,40000,50000,60000]
tempos=[]
def geraLista(tamanho):
  x=[]
  for i in range(tamanho): x.append(i)
  random.shuffle(x)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def radixSort(lista):
    bottom = 1
    top = max(lista)

    while top/bottom > 0:
        indice = len(lista) + 1
  
        ocorrencias = [0] * indice

        for i in lista:
            ocorrencias[i] += 1

        k = 0

        for i in range(indice):
            for j in range(ocorrencias[i]):
                lista[k] = i
                k += 1
        
        bottom *= 10

for i in tamanhos:
  #print("comecei")
  lista=geraLista(i)
  #lista=geraListaPiorCaso(i)
  #print("terminei")
  #print("comecei dnv")
  now=time.time()
  radixSort(lista)
  then=time.time()
  #print(lista)
  #print("acabei dnv")
  tempos.append(then-now)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
