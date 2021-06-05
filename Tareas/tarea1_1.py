solucion = [1,2,3,4]
ni = [1,4,2,3]

print ("Estado inicial")
print(ni)
print()

def profundidad(entrada, solucion):

	nodo_actual = []
	nodos_frontera = []
	nodos_visitados = []
	nodos_frontera.append(ni)
	nodo_front_cop = [ni]
	nodos_visitados=[]
	tam = len(ni) - 1
	while len(nodos_frontera) != 0:
		nodo_actual = nodos_frontera.pop()
		if nodo_actual == solucion:
			print("Nodos visitados")
			print(nodos_visitados)
			print()
			print("Nodos frontera")
			print(nodo_front_cop)
			return nodo_actual
		else:
			nodos_visitados.append(nodo_actual)

		hijo = nodo_actual.copy()
		for i in range(tam):
			hijo[i],hijo[i+1] = hijo[i+1],hijo[i]
			print (hijo)
			if (not(hijo in nodos_frontera) and not(hijo in nodos_visitados)):
				nodos_frontera.append(hijo)
				nodo_front_cop.append(hijo)
			hijo = nodo_actual.copy()
	print("Nodos visitados")
	print(nodos_visitados)
	print()
	print("Nodos frontera")
	print(nodos_frontera)
	return "no hay solucion"

solucion = profundidad(ni, solucion)
print("La solucion es: ")
print(solucion)