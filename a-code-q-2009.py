archivo=open('a-small-q-2009.in')

lista=[]

for linea in archivo.readlines():
	lista.append(linea)
	
NumPalabras=int(lista[0].split()[1])

#~ Crea lista de palabras
Palabras=lista[1:NumPalabras+1]

#~ Crea lista de patrones
Patrones=lista[NumPalabras+1:]

def SaleDelParentesis (j, patron):
#~ Dado un patron y un indice j, devuelve el proximo indice fuera del parentesis
	for i in range (j+1, len (patron)):
		if patron[i]==')':
			return i+1
		
def match (patron, palabra):
#~ Devuelve True si el patron y la palabra matchean y caso contrario, devuelve False
	i=0
	j=0
	ultimoParentesis=')'
	while i<len(palabra):
		if ultimoParentesis==')':
			if patron[j]=='(':				
				ultimoParentesis='('
			else:
				if patron[j]==palabra[i]:
					i+=1					
				else:
					return False
			j+=1
		else:
			if patron[j]==')':
				return False
			else:
				if patron[j]==palabra[i]:
					j=SaleDelParentesis (j, patron)
					ultimoParentesis=')'
					i+=1				
				else:
					j+=1
	return True
				
for a in range (len(Patrones)):
	contador=0
	for palabra in Palabras:
		if match (Patrones[a], palabra):
			contador+=1
	print  "Case #%d:" % (a+1), contador
				

		






	
	
	
	
