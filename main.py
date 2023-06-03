import logging
import random

try:
    logging.basicConfig(
        level=logging.DEBUG,
        filename='log.log',
        filemode='w',
        format='%(message)s'
    )


    class Power:
        def __init__(self):
            self.energy = 120

        def consume_energy(self, amount):
            self.energy -= amount
            if self.energy < 0:
                self.energy = 0


    class Cat(Power):
        def __init__(self):
            super().__init__()
            self.distance = 0
            self.food = 0

        def go(self):
            logging.debug('Going..')
            self.distance += 1
            self.food += random.randint(1, 7)
            self.consume_energy(10)

        def live_a_day(self, day):
            logging.info('''
                New day
            ''')
            logging.debug(f'Day {day}:')
            self.go()
            if self.energy > 0:
                self.go()
                if self.food >= 10:
                    self.status()
            else:
                logging.critical('Cat has died due to lack of energy.')


        def status(self):
            logging.debug(f'Path: {self.distance}')
            logging.debug(f'Food: {self.food}')
            logging.debug(f'Energy: {self.energy}')
            logging.debug('''                                             
                         ,     ,
                         |\\_,-/|
                         / _  _ |    ,--.
                        (  @  @ )   / ,-'
                         \  _T_/-._( (
                         /         `. \\
                        |         _  \ |
                         \ \ ,  /      |
                          || |-_\__   /
                         ((_/`(____,-'             
         ''')


    cat = Cat()
    for day in range(1,8):
        cat.live_a_day(day)


except NameError:
    print("Помилка: Змінна не визначена.")
except ValueError:
    print("Помилка: Щось не то з числами.")
except IndexError:
    print("Помилка!")
