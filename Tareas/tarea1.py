solucion = [1,2,3,4]
ni = [1,4,2,3]

print ("Estado inicial")
print(ni)
print()

tam = len(ni) - 1
n0 = [x for x in range(tam)]
nodo_frontera = [ni]
nodo_front_cop = [ni]
nodos_visitados=[]


flag = False
while flag is not True:
	ni = nodo_frontera[0]
	nodo_frontera.remove(nodo_frontera[0])
	if (ni == solucion):
		print("La solucion es ")
		print(ni)
		print()
		flag = True
	nodos_visitados.append(ni)
	hijo = ni.copy()

	for i in range(tam):
		
		hijo[i],hijo[i+1] = hijo[i+1],hijo[i]
		print (hijo)
		
		if (not(hijo in nodo_frontera) and not(hijo in nodos_visitados)):
			nodo_frontera.append(hijo)
			nodo_front_cop.append(hijo)


		hijo = ni.copy()

print("Nodo frontera")
print(nodo_front_cop)

print("Nodos visitados")
print(nodos_visitados)
