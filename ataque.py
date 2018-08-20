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
    ini = classemonstros.monsters.dragon
ataque = input('Não!! um {} apareceu, vamos atacalo, você pode usar as mão ou magia, ataque agora, ele vai nos destruir'.format(inimigo))
print(ini.vidain)
while ini.vidain >0:
    if ataque == ('magia'):
        print('Você jogou uma bola de fogo no {}'.format(inimigo))
        dados = random.randint(1, 12)
        ataque =(player.magiap + player.inteligencia/2) * dados         
        print('Você tirou {} nos dados,  seu ataque causou {} de danos no {}'.format(dados, ataque, inimigo))
        ini.vidain -= ataque
        if ini.vidain <=0:
            print('O {} morreu'.format(inimigo))
        else:
            ataque = input('o {} ainda tem {} de vida, ataque novamente, AGORA!!!'.format(inimigo, ini.vidain))    


    
    
