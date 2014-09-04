def palindromo (c):
	b=c[::-1]
	if b==c:
		return True
	else:
		return False

print("introduzca la cadena: ")

a=raw_input()
if palindromo(a)==True:
	print("la cadena es palindromo")
else:
	print("la cadena no es palindromo")