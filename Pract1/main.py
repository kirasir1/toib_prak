import hashlib, re, requests, string, random, itertools


def task1():
    string = input('Введите строку: ')
    print(hashlib.sha256(string.encode('utf-8')).hexdigest())


def task2():
    try:
        length = int(input('Введите длину пароля: '))
    except (ValueError):
        length = 8
    print(''.join(random.choice(string.ascii_uppercase + string.ascii_letters +
                                string.punctuation) for i in range(length)))


def task3():
    passtr = input('Введите строку: ')
    regulyarka = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-+_!@#$%^&*., ?])[\S]{8,}$')
    if regulyarka.match(passtr):
        print('Действительный пароль')
    else:
        print('Пароль не соответствует требованиям')


def task4():
    file = open('passwds.txt')
    regulyarka = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-+_!@#$%^&*., ?])[\S]{8,}$')
    for line in file:
        if regulyarka.match(line.rstrip()):
            print(line.rstrip())


def task5():
    file = open('creds.txt')
    for line in file:
        pwd = hashlib.sha1(bytes(re.split(',|\n', line, maxsplit=1)[1], encoding='utf-8'))
        rq = requests.get('https://api.pwnedpasswords.com/range/{0}'.format(pwd.hexdigest()[:5]))
        try:
            re.split(':|\r\n', rq.text).index(pwd.hexdigest()[5:].upper())
            print('Leaked password found')
        except ValueError:
            print("Not leaked")


def task6():
    pwd = input('Введите пароль: ')
    for guess in itertools.product(string.ascii_uppercase + string.ascii_letters +
                                   string.punctuation + string.digits, repeat=len(pwd)):
        if ''.join(guess) == pwd:
            print("Password is: {0}".format(''.join(guess)))


def main():
    while True:
        try:
            choice = int(input('Выберите номер задания (от 1 до 6): '))
            match choice:
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 5:
                    task5()
                case 6:
                    task6()
                case _:
                    print("Введите верный номер задания (от 1 до 6)")
        except ValueError:
            print('Введите верный номер задания (от 1 до 6)')


if __name__ == "__main__":
    main()
