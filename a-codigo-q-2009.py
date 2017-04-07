archivo = open('a-small-q-2009.in')

lista = archivo.readlines()

numPalabras = int(lista[0].split()[1])

palabras = lista[1:numPalabras + 1]

patrones = lista[numPalabras + 1:]

def saleDelParentesis(j, patron):
	for i in xrange (j+1, len (patron)):
		if patron[i]==')':
			return i+1
    
def match(patron, palabra):   
    
    indicePalabra = 0
    indicePatron= 0
   
    parentesisAbierto = False
   
    while indicePalabra < len(palabra):
        if parentesisAbierto == False:
            if patron[indicePatron] == '(':
                 parentesisAbierto = True
            else:
                if patron[indicePatron] == palabra[indicePalabra]:
                    indicePalabra += 1
                else:
                    return False
            indicePatron += 1
        else:
            if patron[indicePatron] == ')':
                return False
            else:
                if patron[indicePatron] == palabra[indicePalabra]:
                    indicePatron = saleDelParentesis(indicePatron, patron)
                    parentesisAbierto = False
                    indicePalabra += 1
                else:
                    indicePatron += 1
    return True

for a in range(len(patrones)):

    contador = sum(match(patrones[a], palabra) for palabra in palabras)

    print "Case #{}: {}".format(a+1, contador)
   
