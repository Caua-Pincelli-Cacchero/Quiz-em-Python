from time import sleep

score = 0

def resposta(alternativa):
    if res == certo:
        score += 1
        print(f'Parabéns você acertou. Sua pontuação atual é {score}')
    else:
        print(f'Você errou. Sua pontuação atual é {score}')


print("Bem vindo ao meu Quiz sobre jogos! Serão 5 perguntas para responder.")

certo = "C"

print("Primeira questão: \nQual foi o ano de lançamento do jogo GTA V? \n"
"A) 2010 \nB) 2012\nC) 2013 \nD) 2009 \nE) 2020")

print('-=' * 20)

res = str(input('Digite sua resposta: ')).upper().strip()

print('Pensando....')
sleep(1.5)

resposta("cC")

print('Segunda questão: \nQual a empresa criadora do jogo Valorant? \n'
'A) Riot Games \nB) EA \nC) VALVE \nD) GameFreak \nE) Epic Games')

res = str(input('Digite sua resposta: ')).upper().strip()

