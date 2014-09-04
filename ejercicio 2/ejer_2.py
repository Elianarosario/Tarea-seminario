a=1
b=20
print"------------------------"	
print"a) los numeros son: "
while b>0:
	print a,
	a=a+1
	b=b-1

b=20
print" "
print"------------------------"	
print"b) los numeros son: "
while b>0:
	print b,
	b=b-1

print" "	
print"------------------------"	
print("c)")

def suma1(a,b):
	return a+b
x=raw_input()
y=raw_input()
m=int(x)
n=int(y)
print ("la suma es: ",suma1(m,n))

print" "
print"------------------------"	
print("d)")
def suma2(a,b):
	return (a+b)
x=raw_input()
y=raw_input()
print ("la suma es: ",suma2(x,y))

print" "
print"------------------------"	
print("f)")
def suma3(a,b):
	return (a+b)
x=int(input())
y=float(input())
print ("la suma es: ",suma3(x,y))


