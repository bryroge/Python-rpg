import classemonstros
import classeplayer

''' RPG '''

print('-' * 20)
print(' ' * 3, 'Bem vindo', ' ' * 3)
print(' ')


def menu():
    print(' ')
    print(' RPG GAME. ESCOLHA SUA OPÇÂO')
    print(' ')
    print('1 - criar personagem')
    print('2 - Classes')
    print('3 - continuar jogo')
    menuop = int(input(''))
    return menuop


while True:
    menuop = menu()
    if menuop == 1:
        import novopersonagem
        import ataque
    if menuop == 2:
        ver = input('Digite uma classe para ver seus atributos: ')
        while ver != ('mago') and ver != ('guerreiro'):
            ver = input('Classe não existe, digite uma classe valida (mago, guerreiro)')
        if ver == ('mago'):
            playermg = classeplayer.player.mago
            print('vida: ', playermg.vida)
            print('Força: ', playermg.força)
            print('magia: ', playermg.magiap)
            print('inteligencia: ', playermg.inteligencia)
            print('defesa: ', playermg.defesa)

        elif ver == ('guerreiro'):
            playermg = classeplayer.player.guerreiro
            print('vida: ', playermg.vida)
            print('Força: ', playermg.força)
            print('magia: ', playermg.magiap)
            print('inteligencia: ', playermg.inteligencia)
            print('defesa: ', playermg.defesa)

        elif ver == ('nifrin'):
            playermg = classeplayer.player.nifrin
            print('vida: ', playermg.vida)
            print('Força: ', playermg.força)
            print('magia: ', playermg.magiap)
            print('inteligencia: ', playermg.inteligencia)
            print('defesa: ', playermg.defesa)

        elif ver == ('amazona'):
            playermg = classeplayer.player.amazona
            print('vida: ', playermg.vida)
            print('Força: ', playermg.força)
            print('magia: ', playermg.magiap)
            print('inteligencia: ', playermg.inteligencia)
            print('defesa: ', playermg.defesa)            
                
    if menuop == 3:
        print('em construção')
        



