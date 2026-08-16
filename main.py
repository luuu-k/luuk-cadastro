#ENTRADA DE DADOS
print("INSIRA SEUS DADOS")
nome = input(("Insira seu nome: "))
idade = int(input(("Insira sua idade: ")))
cidade = input(("Insira sua cidade: "))

cadastro = [nome, idade, cidade]

#CONDICIONAMENTO DE DADOS
print("\nVERIFICAÇÃO DE DADOS\n")
#NOME
print(nome)
verificacao = input(("\nSeu nome está correto?(s/n): "))
while verificacao == "n":
    nome = input(("\nReescreva seu nome: "))
    print("")
    print (nome)
    verificacao = input(("\nSeu nome está correto?(s/n): "))
#FIM DO NOME
if verificacao == "s":
#IDADE
    print("")
    print(idade)
    verificacao = input(("\nSua idade está correta?(s/n): "))
    while verificacao == "n":
        idade = int(input(("\nReescreva sua idade: ")))
        print("")
        print (idade)
        verificacao = input(("\nSua idade está correta?(s/n): "))
#FIM DA IDADE
    if verificacao =="s":
#CIDADE
        print("")
        print (cidade)
        verificacao = input(("\nSua cidade está correta?(s/n): "))
    while verificacao == "n":
        cidade = input(("\nReescreva sua cidade: "))
        print (cidade)
        verificacao = input(("\nSua cidade está correta?(s/n): "))
#FIM DA CIDADE
    if verificacao == "s":
            print("Os dados cadastrados foram: ")
            print(nome)
            print(idade)
            print(cidade)
