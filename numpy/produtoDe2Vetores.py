import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

dot = 0
#for e, f in zip(a, b):
   #dot += e * f
# resposta = 11

for i in range(len(a)):
    dot += a[i] * b[i]
# resposta = 11
print("")
print("for i in range(len(a)):")
print("dot += a[i] * b[i]")
print("resposta: ", dot)

print("\n a * b : ", a*b)
# resposta = [3 8]

print("\n np.sum(a*b) : ", np.sum(a*b))
# resposta = 11

print("\n (x*x).sum() : ", (a*b).sum())
# resposta = 11

print("\n np.dot(x, x) : ", np.dot(a, b))
# resposta = 11

print("\n x.dot(x) : ", a.dot(b))
# resposta = 11

print("\n @ : ", a @ b)
# resposta = 11