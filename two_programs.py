import random
from sys import argv

# новый комментарий для гитхаба
def guess(min_numb, max_numb=10, count=3):
    numb_1 = random.randint(min_numb, max_numb)
    for i in range(count):
        nubm = int(input('Enter number: '))
        if nubm == numb_1:
            return True
        elif nubm > numb_1:
            print('Число меньше загаданного')
        else:
            print('Число больше загаданного')
    return False


if __name__ == '__main__':
    print(guess(*list(map(int, argv[1:]))))

