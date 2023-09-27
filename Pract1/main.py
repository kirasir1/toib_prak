import random
import string
while True:
    try:
        length = int(input('Введите длину пароля: '))
    except (ValueError):
        length = 8
    print(''.join(random.choice(string.ascii_uppercase + string.ascii_letters +
                                string.punctuation) for i in range(length)))