primero=0
segundo=1
i=0
print(primero)
for i in range(1,16,1):
  numero=primero + segundo
  segundo=primero
  primero=numero
  print(numero)
