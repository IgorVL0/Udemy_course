# Entrada de dado
#print("Qual seu nome?")
#nome = input()
nome = input("Qual o seu nome? ")

# Saida
#print("Seja bem-vindo(a) %s" % nome)
print(f'Seja bem vindo(a) {nome}')

#print("Qual a sua idade?")
#idade = input()
idade = input("Qual sua idade? ")

#print("O(A) %s tem %s anos" % (nome, idade))
print(f'O(A) {nome} tem {idade} anos')
print(f"O {nome} nasceu em {2020-int(idade)}")
