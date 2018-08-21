import random
import classemonstros
import classeplayer
import novopersonagem
import time
player = novopersonagem.player
lista = ['orc', 'dragon']
inimigo = random.choice(lista)
print(inimigo)
if inimigo == ('orc'):
    ini = classemonstros.monsters.orc
elif inimigo == ('dragon'):
    ini = classemonstros.monsters.dragão
ataque = input('Não!! um {} apareceu, vamos atacalo, você pode usar as mãos ou magia, ataque agora, ele vai nos destruir'.format(inimigo))
print('vida ini', ini.vidain)
print('ataque player', player.atk)
while ini.vidain > 0 and player.vida > 0:
    
    if ataque == ('magia'):
        dados = random.randint(1, 12)
        print('Você jogou uma bola de fogo no {}'.format(inimigo))         
        ataque = player.atk * dados - ini.defe
        if ataque <= 0 and player.vida > 0:
            print('Você tirou {} nos dados.'.format(dados))
            print(' Você errou o ataque.')
            print('O {} esta atacando... Nós vamos morrer!!!'.format(inimigo))
            time.sleep(2)
            danoini = (ini.força + ini.magiain) / 8 * dados
            print('dano ini', danoini)
            recebdano = danoini - player.defesa + player.força
            player.vida -= recebdano
            print('dados:', dados)
            if player.vida <= 0:
                print('O {} causou um dano de {}, e você caiu morto, bem, parece que você não era tão poderoso assim...'.format(inimigo, recebdano, player.vida))
            else:
                print('O {} causou um dano de {}, você ainda tem {} de vida'.format(inimigo, recebdano, player.vida))
            ataque = input('ataque novamente, e vê se não erra dessa vez!!')
        elif ataque > 0 and player.vida > 0:
            print('Você tirou {} nos dados,  seu ataque causou {:.2f} de danos no {}'.format(dados, ataque, inimigo))
            ini.vidain -= ataque
            if ini.vidain <= 0:
                print('O {} morreu'.format(inimigo))
            else:
                print('o {} ainda tem {:.2f} de vida.'.format(inimigo, ini.vidain))
                print('O {} esta atacando... Nós vamos morrer!!!'.format(inimigo))
                time.sleep(2)
                danoini = (ini.força + ini.magiain) / 8 * dados
                print('dados:', dados)
                print('dano ini', danoini)
                recebdano = danoini - player.defesa + player.força
                player.vida -= recebdano
                if player.vida <= 0:
                    print('O {} causou um dano de {}, e você caiu morto, bem, parece que você não era tão poderoso assim...'.format(inimigo, recebdano, player.vida))
                else:
                    print('O {} causou um dano de {}, você ainda tem {} de vida'.format(inimigo, recebdano, player.vida))
                    ataque = input('Ataque novamente, AGORA!!!')

        
'''while player.vida > 0:       
            print('O {} esta atacando... Nós vamos morrer!!!'.format(inimigo))
            danoini = (ini.força + ini.magiain) / 4 * dados
            print('dano ini', danoini)
            recebdano = danoini - player.defesa + player.força
            player.vida -= recebdano
            print('dados:', dados)
            if player.vida <= 0:
                print('O {} causou um dano de {}, e você caiu morto, bem, parece que você não era tão poderoso assim...'.format(inimigo, recebdano, player.vida))
            else:
                print('O {} causou um dano de {}, você ainda tem {} de vida'.format(inimigo, recebdano, player.vida))'''


