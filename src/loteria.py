'''
Programa para gerar uma interação divertida com o computador, criando um numero da sorte e dando ao
usuario a chance de acertar, com uma mensagem ao final indicando se acertou ou errou
'''

# %%

# Numero da sorte que o usuário tentará acertar (hardcoded)
numero_da_sorte = 7

# Limitar as chances do usuário a, no maximo 3   
for tentativa in range(3):

    try:
        
        # Input para o usuário digitar o número
        numero_usuario = int(input(f"Tentativa {tentativa + 1 }: Digite um número entre 1 e 15, por favor"))

        # Teste do resultado com o print, indicando a direção do erro
        if numero_usuario == numero_da_sorte:
            print("Parabéns, você acertou o resultado")
        elif numero_usuario > numero_da_sorte :
            print("Que pena, você errou. Tente um número menor na próxima vez")
        else:
            print("Que pena, você errou. Tente um número maior na próxima vez") 

    except ValueError as err:
        print("Insira um valor numérico inteiro para fazer o teste")
# %%
