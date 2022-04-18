# Faça um programa em Python para ler a quantidade atual em estoque, a quantidade máxima em estoque e a quantidade mínima em estoque de um produto. 
# Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). 
# Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

estoque = int(input("Digite o estoque: "))
minima = input("Digite a quantidade minima: ")
maxima = input("Digite a quantidade maxima ")

media = (int(maxima) + int(minima)) / 2

if (estoque >= media):
  print("Não efetuar compra")
else:
  print("Efetuar compra")
