'''
Programa para gerar uma interação divertida com o computador, criando um numero da sorte e dando ao
usuario a chance de acertar, com uma mensagem ao final indicando se acertou ou errou
'''

# %%

# Numero da sorte que o usuário tentará acertar (hardcoded)
numero_da_sorte = 7

# Input 1 : Numero de tentativas variavel, com validação
while True:
    try:
        creditos = int(input("Digite o numero de créditos"))
        # Ao passar na validação, sair do while e continuar o fluxo
        break
    except ValueError as err:
        print("Por favor, insira um valor válido para a quantidade de créditos")

creditos_restantes = creditos

# Limitar as chances do usuário a, no maximo 3   
for tentativa in range(creditos):

    # Input para o usuário digitar o número, gastando crédito somente com valores válidos
    while True:
        try:
            numero_usuario = int(input(f"Tentativa {tentativa+1}: Digite um número entre 1 e 15, por favor"))
            break
        except ValueError as err:
            print("Por favor, insira um valor válido entre 1 e 15.\nSeu crédito atual não foi consumido")

    # Consumir um credito
    creditos_restantes -= 1

    # Teste do resultado com o print, indicando a direção do erro e detalhando o acerto
    if numero_usuario == numero_da_sorte:
        print(f"Parabéns, você acertou o resultado {numero_usuario} na tentativa #{tentativa+1}!")
        break
    
    # Testar se ainda existem créditos para uso
    elif creditos_restantes > 0:
        if numero_usuario > numero_da_sorte :
            print("Que pena, você errou. Tente um número menor na próxima vez...")
            print(f"Crédito(s) restante(s) : {creditos_restantes}")
        else:
            print("Que pena, você errou. Tente um número maior na próxima vez...") 
            print(f"Crédito(s) restante(s) : {creditos_restantes}")
    else:
        print(f"GAME OVER: Você não tem mais tentativas. O número da sorte era {numero_da_sorte}")
        print("Para começar outro jogo compre mais fichas")