archivo=open('C-large-practice.in')

lista=[]

for linea in archivo.readlines():
	lista.append(linea)
	
string='welcome to code jam'
tope=len(string)+1


	
def funcion (case):
	diccionario={}
	for i in range (1, tope):
		diccionario[i]=[0]*(len (case)+1)
	for i in range (1, len (case)):
			if string[0]==case[i-1]:
				diccionario[1][i]=1+diccionario[1][i-1]
			else:
				diccionario[1][i]=diccionario[1][i-1]
	longitud=2
	while longitud < tope:
		for i in range (longitud, len (case)+1):
			if string[longitud-1]==case[i-1]:
				diccionario[longitud][i]=diccionario[longitud-1][i-1]+diccionario[longitud][i-1]
			else:
				diccionario[longitud][i]=diccionario[longitud][i-1]
		longitud+=1
	return ('000'+str(diccionario[tope-1][len(case)]))[-4:]
					

for i in range (1, len (lista)):
	print 'Case #%i:'%(i), funcion (lista[i])
	
				
