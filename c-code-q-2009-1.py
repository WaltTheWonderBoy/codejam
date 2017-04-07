archivo=open('C-large-practice.in')

archivo.readline()

testCases=archivo.readlines()

leyenda='welcome to code jam'
	
def _funcion (case):
	#~ Devuelve %1000, la cantidad de veces que aparece 'welcome to code jam' en el testcase
	dicc={}
	
	for i in xrange (len(leyenda)):
		dicc[i+1]=([0]*(len (case)+1) 
	for i in xrange (1, len (case)):
			if case[i-1]==leyenda[0]:
				dicc[1][i]=1+dicc[1][i-1]
			else:
				dicc[1][i]=dicc[1][i-1]				
	for longitud in xrange (2, len(leyenda)+1):
		for i in xrange (longitud, len (case)+1):
			if case[i-1]==leyenda[longitud-1]:
				dicc[longitud][i]=dicc[longitud-1][i-1]+dicc[longitud][i-1]
			else:
				dicc[longitud][i]=dicc[longitud][i-1]
	return ('000'+str(dicc[len(leyenda)][len(case)]))[-4:]
		
for numCase, case in enumerate(testCases):
	print "Case #{}: {}".format(numCase+1, _funcion (case))
	
