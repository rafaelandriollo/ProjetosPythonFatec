# Faça um programa em Python, que calcule o quadrado de um número usando o método que define que o quadrado de um número positivo n é igual à soma dos n primeiros números ímpares.
# Exemplos:
# 32 = 1 + 3 + 5
# 62 = 1 + 3 + 5 + 7 + 9 + 11
# Obs. 1: Faça a validação para a entrada do valor n, ser somente positivo. Se for <= 0, pedir a entrada novamente do valor.
# Obs. 2: Não use a função pow e nem ** para calcular o quadrado do número.

i=0
soma=0
val=1

while (True): #validação de número positivo 
  num = int(input("Digite um numero: "))
  
  if (num >= 0):
    break
  else:
    print ("numero invalido")

while (i<num): #rodar até os n primeiros numeros ímpares
  if (val%2==1): #testar se o número é ímpar
    soma = soma + val
    i = i+1
  val = val + 1

print("O quadrado de ", num, " é ", soma)
