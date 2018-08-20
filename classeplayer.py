
class player():
    class mago:
        nome = ('Mago')
        vida = 6
        magiap = 5
        força = 2.5
        inteligencia = 4
        defesa = 2
        atk = ((força / 2 + magiap * 2) / 2) + magiap * 0.15 + força * 0.05

    class guerreiro:
        nome = ('Guerreiro')
        vida = 8
        magiap = 2.5
        força = 4.5
        defesa = 3
        inteligencia = 1.5
        atk = ((força * 2 + magiap / 2) / 2) + força * 0.1 + magiap * 0.05

    class Amazona:
        nome = ('Amazona')
        vida = 7
        magiap = 2.5
        força = 3.5
        defesa = 3.5
        inteligencia = 2.5


    class nifrin:
        nome = ('Nifrin')
        vida = 6.5
        magiap = 4
        força = 3
        defesa = 3.5
        inteligencia = 2.5