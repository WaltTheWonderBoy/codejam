from collections import defaultdict

archivo=open('C-large-practice.in')
archivo.readline()

inputLines=[]

for line in archivo.readlines():
	inputLines.append(line.split())
	
def log(x):		
	i=0
	while x>1:
		x/=2
		i+=1
	return i

def _partition(n):
	if n==0:
		return (0,0)
	if n%2==0:
		return ((n/2)-1, n/2)
	else:
		return (n/2, n/2)

def _mainFunction(N, K):
	
	dicc=defaultdict(int)	
	
	tree=[0]*(2+2*log(K))	
	tree[1]=_partition(N)
	
	if K==1:
		return  max (tree[1]), min (tree[1])
	
	tree[2]=_partition(tree[1][0])
	tree[3]=_partition(tree[1][1])
		
	for i in xrange( 1, 4):
		for num in tree[i]:
			dicc[num]+=1		
		
	for i in xrange (4, 2*log(K)+2, 2):
			tree[i]=_partition(tree[i-2][0])			
			tree[i+1]=_partition(tree[i-1][1])
			if tree[i][0]==tree[i][1]==tree[i+1][0]:
				if tree[i+1][1]==tree[i][0]:
					dicc[tree[i][0]]+=2*(2**(i/2))
				else:
					dicc[tree[i][0]]+=2*dicc[tree[i-2][0]]+dicc[tree[i-1][1]]
					dicc[tree[i+1][1]]+=dicc[tree[i-1][1]]
			elif tree[i][0]==tree[i+1][0] and tree[i][1]==tree[i+1][1]:
				dicc[tree[i][0]]+=2**(i/2)
				dicc[tree[i][1]]+=2**(i/2)	
			else:
				dicc[tree[i][0]]+=dicc[tree[i-2][0]]
				dicc[tree[i][1]]+=dicc[tree[i-2][0]]+2*dicc[tree[i-1][1]]				
		
	if K-2**log(K)< dicc[tree[2*log(K)-1][1]]:
		return max (tree[-1][0], tree[-1][1]), min (tree[-1][0], tree[-1][1])
		
	return max (tree[-2][0], tree[-2][1]), min (tree[-2][0], tree[-2][1])  			
		
for numCase, case in enumerate(inputLines):
	print "Case #{}: {} {}".format(numCase+1, _mainFunction (int(case[0]), int(case[1]))[0], _mainFunction (int(case[0]), int(case[1]))[1])




