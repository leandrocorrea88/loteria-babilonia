'''
Programa para gerar uma interação divertida com o computador, criando um numero da sorte e dando ao
usuario a chance de acertar, com uma mensagem ao final indicando se acertou ou errou
'''

# %%

import random as rnd

# %%
def valida_formato(msg_entrada):
    """ Função que valida o formato de entrada dos créditos digitados pelo usuário """
    while True:
        try:
            resultado = int(input(msg_entrada))
            # Ao passar na validação, sair do while e continuar o fluxo
            return resultado
        except ValueError as err:
            print("Por favor, insira um valor válido para a quantidade de créditos")


def valida_formato_e_intervalo(msg_entrada, limite_inferior, limite_superior):
    """ Função que valida o formato de entrada e intervalo das tentativas do usuário """
    while True:
        
        # Testar formato
        try:
            resultado = int(input(msg_entrada))
        except ValueError as err:
            print("Por favor, insira um valor válido para acertar o número da sorte.\nSeu crédito atual não foi consumido")
            continue

        # Se passar, testar o intervalo
        if limite_inferior <= resultado <= limite_superior:
            return resultado
        else:
            print(f"Insira um valor entre {limite_inferior} e {limite_superior}.\nSeu crédito atual não foi consumido")

# %%
# Numero da sorte que o usuário tentará acertar (aleatório)
numero_da_sorte = rnd.randint(a=1 , b=15)

# Input 1 : Numero de tentativas variavel, com validação
creditos = valida_formato("Digite o numero de créditos")
creditos_restantes = creditos

# Limitar as chances do usuário a, no maximo 3   
for tentativa in range(creditos):

    # Input para o usuário digitar o número, gastando crédito somente com valores válidos
    numero_usuario = valida_formato_e_intervalo(msg_entrada=f"Tentativa {tentativa+1}: Digite um número entre 1 e 15, por favor",
                                                limite_inferior=1, limite_superior=15)

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
