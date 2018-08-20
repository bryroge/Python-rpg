import random
import classemonstros
import classeplayer
import novopersonagem

player = novopersonagem.player
lista = ['orc', 'dragon']
inimigo = random.choice(lista)
print(inimigo)
if inimigo == ('orc'):
    ini = classemonstros.monsters.orc
elif inimigo == ('dragon'):
    ini = classemonstros.monsters.dragão
ataque = input('Não!! um {} apareceu, vamos atacalo, você pode usar as mãos ou magia, ataque agora, ele vai nos destruir'.format(inimigo))
print(ini.vidain)
print(player.atk)
while ini.vidain > 0:
    if ataque == ('magia'):
        print('Você jogou uma bola de fogo no {}'.format(inimigo))
        dados = random.randint(1, 12)
        ataque = player.atk * dados - ini.defe
        if ataque <= 0:
            print('Você tirou {} nos dados.'.format(dados))
            ataque = input(' Você errou o ataque, ataque novamente, e vê se não erra dessa vez!!')
        elif ataque >= 0:
            print('Você tirou {} nos dados,  seu ataque causou {:.2f} de danos no {}'.format(dados, ataque, inimigo))
            ini.vidain -= ataque
            if ini.vidain <= 0:
                print('O {} morreu'.format(inimigo))
            else:
                ataque = input('o {} ainda tem {:.2f} de vida, ataque novamente, AGORA!!!'.format(inimigo, ini.vidain))




