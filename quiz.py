from time import sleep

score = 0

print("Bem vindo ao meu Quiz sobre jogos! Serão 5 perguntas para responder.")

print("Primeira questão: \nQual foi o ano de lançamento do jogo GTA V? \n"
"A) 2010 \nB) 2012\nC) 2013 \nD) 2009 \nE) 2020")

certo = 'C'

print('-=' * 20)

resposta_usuario = str(input('Digite sua resposta: ')).upper().strip()

print('-=' * 20)
print('Pensando....')
sleep(1.5)

if resposta_usuario == certo:
    score += 1
    print(f'Você acertou! Sua pontuação é {score}')
else:
    print(f'Você errou! Sua pontuação é {score}')

print('-=' * 20)

print('Segunda questão: \nQual a empresa criadora do jogo Valorant? \n'
'A) Riot Games \nB) EA \nC) VALVE \nD) GameFreak \nE) Epic Games')

certo = 'A'

resposta_usuario = str(input('Digite sua resposta: ')).upper().strip()

print('-=' * 20)
print('Pensando....')
sleep(1.5)

if resposta_usuario == certo:
    score += 1
    print(f'Você acertou! Sua pontuação é {score}')
else:
    print(f'Você errou! Sua pontuação atual é {score}')

print('-=' * 20)

print('Terceira questão: \nQuem ganhou o GOTY(Game Of The Year) de 2018? \n'
'A)Red Dead Redemption II \nB) God Of War \nC) Fortnite \nD) Celeste \nE) Overcoocked 2')

certo = 'B'

resposta_usuario = str(input('Digite sua resposta: ')).upper().strip()

print('-=' * 20)
print('Pensando....')
sleep(1.5)

if resposta_usuario == certo:
    score += 1
    print(f'Você acertou! Sua pontução é {score}')
else:
    print(f'Você errou! Sua pontuação é {score}')

print('-=' * 20)

print('Quarta questão: \nQuem foi o único campeão mundial de Fortnite? \n'
'A) Blackoutz \nB) Tifuu \nC) Ninja \nD) King (argentino) \nE) Bulga')

certo = 'E'

resposta_usuario = str(input('Digite sua resposta: ')).upper().strip()

print('-=' * 20)
print('Pensando....')
sleep(1.5)

if resposta_usuario == certo:
    score += 1
    print(f'Você acertou! Sua pontuação é {score}')
else:
    print(f'Você errou! Sua pontuação é {score}')

print('-=' * 20)

print('Quinta e ultima questão: \nQual jogo de celular explodiu em 2015? \n'
'A) Clash of Clans \nB) Pokemon GO \nC) Mobile Legends \nD) Clash Royale \nE) Brawl Stars')

certo = 'D'

resposta_usuario = str(input('Digite sua resposta: ')).strip().upper()

print('-=' * 20)
print('Pensando....')
sleep(1.5)

if resposta_usuario == certo:
    score += 1
    print(f'Você acertou! Sua pontuação é {score}')
else:
    print(f'Você errou! Sua pontuação é {score}')

print('-=' * 20)

if score == 0 or 1 or 2:
    print('Você precisa saber mais sobre jogos, mas boa tentativa!')
elif score == 3:
    print('Você está indo bem, continue melhorando!')
elif score == 5:
    print('Você manja mesmo de jogos! Parabéns por ter concluido sem nenhum erro!')
