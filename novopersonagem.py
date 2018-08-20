import classeplayer
esnome = input('Escolha seu nome: ')
classe = input('Olá {}, dentre as classes: Mago, Guerreiro, Nefrin e Amazona, qual você escolhe?'.format(esnome))
classe.lower()
if classe == ('mago'):      
    player = classeplayer.player.mago
    print('Mago tem vida inicial de: ', classeplayer.player.mago.vida)
elif classe == ('guerreiro'):
    player = classeplayer.player.guerreiro
    print(classeplayer.player.guerreiro)
elif classe == ('amazona'):
    player = classeplayer.player.amazona
    print(classeplayer.player.amazona)
elif classe == ('nifrin'):
    player = classeplayer.player.nifrin
    print(classeplayer.player.nifrin)
else:
    print('Classe não conhecida, escolha uma classe valida: ')
    classe = input(' ')
print('Eis que nasce o grande {}, e eles o chamam {}. Vá, Grande {}, Livre o mundo do mal'.format(classe, esnome, classe))
