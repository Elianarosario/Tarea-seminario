

def numeros(a,b):
	ini=a
	fin=b
	while ini<=fin:
		print ini,
		ini=ini+1 
def pares(a,b):
	ini=a
	fin=b
	while ini<=fin:
		if ini%2==0:
			print ini,
		ini=ini+1
print "introduzca un rango: "
x=input()
y=input()
print "los numeros son:  "
numeros(x,y)
print" "
print"------------------------------------------"
print "los numeros pares son: "
pares(x,y)