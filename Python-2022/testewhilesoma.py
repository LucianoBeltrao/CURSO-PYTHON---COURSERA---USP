def main():
	num = int(input("Digite um número para somar: "))
	soma = 0
	while num != 0:
		soma = soma + num
		num = int(input("Digite um número para somar: "))
	print("A soma dos números é", soma)
main()
