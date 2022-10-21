import numpy as np

L = [ 1, 2 ,3 ]

for e in L:
    print(e)
print("")

A = np.array([1,2,3])

for e in A:
    print(e)
print("")

print("\n", L)
print("\n", A)

L.append(4)
print("\n", L)
# A.append(4) nao pode usar no array np[]

print("\n", L + [5]) # adicona o elemento separado

print("\n", A + np.array([4])) # ja no numpy adicona o valor a todos os elementos

print("\n", A + np.array([4, 5 ,6])) # adiciona vetorialmente cada elemento

print("\n",2 * A) # multiplicar todos os elementos

print("\n", 2 * L) # se realizarmos o mesmo em uma lista normal ele vai duplicar a lista
print("\n", L + L) # mesmo com L + L

L2 = []

#for e in L:
    #L2.append(e + 3) #outra forma de fazer:

##L2 = [e + 3 for e in L]

for e in L:
    L2.append(e**2) # com potencia
print("\n", L2)

print("\n", A**2) # mesma coisa do de cima com numpy

print("\n",np.sqrt(A)) # pegar a raiz de todos os elementos

print("\n", np.log(A)) # pegar o log de todos os elementos

print("\n", np.exp(A)) # pegar o exponencioal de todos os elementos

print("\n", np.tanh(A)) # pegar a tangente de todos os elementos
