#faca um programa que pede o usuario para escolhar uma classe
#com base no numero que ele escolher, sendo:
#1 - mago //2 - barbaro // 3 - arqueiro
#insira um número para escolher a classe:
print("Escolha sua classe para jogar!")
print("1 - Barbaro!")
print("2 - Mago!")
print("3 - arqueiro!")
#usuario ira digitar um numero para escolher sua classe abaixo
numero = int(input("digite um número: "))
if numero==1:
       classe="Barbaro"
elif numero==2:
       classe="Mago"
elif numero==3:
       classe="Arqueiro"
else:
       classe="Invalida"
print(f"A classe que você escolheu é {classe} \n")

#usuario ja escolheu sua classe
#agora ele tera que escolher seus equipamentos
print("Agora escolha qual tipo de equipamento irá usar!")
print("1 - Machado")
print("2 - Cajado")
print("3 - Arco e Flecha")
print("4 - Espada e Escudo")
equip = int(input("Escolha seu equip.: "))
if(equip==1):
       estilo="Machado"
elif(equip==2):
       estilo="Cajado"
elif(equip==3):
       estilo="Arco e Flecha"
elif(equip==4):
       estilo="Espada e Escudo" 
else:
       estilo="Invalida"
#retornar uma mensagem de erro caso o usuario nao atenda aos requisitos.       
if estilo != "Invalida" and classe != "Invalida":
        print(f"\n Personagem criado com sucesso! \n Vocé um {classe} com o equipamento {estilo}")
else:
    print("Erro na criação do personagem, tente novamente!")
print("Você esta pronto para aventura!")
#print(f"Você jogara de {classe} e usará {estilo}")
#print("Hora da aventura!")


       