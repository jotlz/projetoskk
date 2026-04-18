n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

###1° Equação:
resultado = 0
expressao = ""
for i in range(n2):
    resultado = resultado + n1
    expressao += f"{n1} + "
print(f"{n1}*{n2} = {resultado}")