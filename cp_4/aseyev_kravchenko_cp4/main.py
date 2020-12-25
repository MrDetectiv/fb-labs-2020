from math import gcd
from random import *
pq = []


def Euclid_Sub(number, field):
    if number == 0:
        return field, 0, 1
    else:
        nod, x, y = Euclid_Sub(field % number, number)
        return nod, y - (field // number) * x, x


def Euclid(number, field):
    nod, x, y = Euclid_Sub(number, field)
    return x % field


def Number_Generator(bits):
    numb = int(getrandbits(bits))
    numb = int(numb | 1 | (1 << (bits - 1)))
    if numb % 2 == 0 or numb % 3 == 0 or numb % 5 == 0 or numb % 7 == 0:
        with open("log.txt", "a") as log:
            log.write(hex(numb))
        return Number_Generator(bits)
    else:
        S = 0
        d = numb - 1
        while d % 2 == 0:
            d //= 2
            S += 1
        for k in range(0, bits - 1):
            a = randint(2, numb - 1)
            x = pow(a, d, numb)
            if x == 1 or x == numb - 1:
                continue
            for i in range(0, S - 1):
                x = pow(x, 2, numb)
                if x == numb - 1:
                    break
            else:
                with open("log.txt", "a") as log:
                    log.write(hex(numb))
                return Number_Generator(bits)
        return numb


def PQ_Generator(bits):
    if not pq:
        with open("log.txt", "w+") as log:
            log.write("This is a log file for non-prime generated numbers!\n")
        pq.append(Number_Generator(bits))
        pq.append(Number_Generator(bits))
        p, q = Number_Generator(bits), Number_Generator(bits)
        while p > pq[0]:
            p = Number_Generator(bits)
        pq.append(p)
        while q > pq[1]:
            q = Number_Generator(bits)
        pq.append(q)
    else:
        pq.clear()
        return PQ_Generator(bits)


def Key_Generator(bits):
    PQ_Generator(bits)
    global A_open_key, B_open_key, A_secret_key, B_secret_key
    Euler_A = (pq[2] - 1) * (pq[3] - 1)
    Euler_B = (pq[0] - 1) * (pq[1] - 1)
    n = pq[2] * pq[3]
    n1 = pq[0] * pq[1]
    e, e1 = 0, 0
    while gcd(e, Euler_A) != 1:
        e = randint(2, Euler_A - 1)
    while gcd(e1, Euler_B) != 1:
        e1 = randint(2, Euler_B - 1)
    d = Euclid(e, Euler_A)
    d1 = Euclid(e1, Euler_B)
    A_open_key = [e, n]
    B_open_key = [e1, n1]
    A_secret_key = [d, n]
    B_secret_key = [d1, n1]
    return A_open_key, B_open_key, A_secret_key, B_secret_key


def Encrypt(m, open_key):
    return pow(m, open_key[0], open_key[1])


def Decrypt(c, secret_key):
    return pow(c, secret_key[0], secret_key[1])


def Sign(m, secret_key):
    return pow(m, secret_key[0], secret_key[1])


def Verify(m, s, open_key):
    t = pow(s, open_key[0], open_key[1])
    if t == m:
        return True
    else:
        return False


def Send_Key(k, sender_secret_key, recipient_open_key):
    s = Sign(k, sender_secret_key)
    s1 = Encrypt(s, recipient_open_key)
    k1 = Encrypt(k, recipient_open_key)
    secret_message = [s1, k1]
    return secret_message


def Receive_Key(secret_message, recipient_secret_key, sender_open_key):
    k = Decrypt(secret_message[1], recipient_secret_key)
    s = Decrypt(secret_message[0], recipient_secret_key)
    return Verify(k, s, sender_open_key)


def Menu():
    choice = int(input("""\n\n\n\n\n\n\n\n\n\n __      __   _                    _                        ___  ___   _     _            _                   _        _   _           
 \ \    / /__| |__ ___ _ __  ___  | |_ ___   ___ _  _ _ _  | _ \/ __| /_\   (_)_ __  _ __| |___ _ __  ___ _ _| |_ __ _| |_(_)___ _ _   
  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ / _ \ || | '_| |   /\__ \/ _ \  | | '  \| '_ \ / -_) '  \/ -_) ' \  _/ _` |  _| / _ \ ' \  
   \_/\_/\___|_\__\___/_|_|_\___|  \__\___/ \___/\_,_|_|   |_|_\|___/_/ \_\ |_|_|_|_| .__/_\___|_|_|_\___|_||_\__\__,_|\__|_\___/_||_| 
                                                                                    |_|                                                \n\n\nChoose an option:\n1 --- Use RSA locally\n2 --- Use RSA with RSA Testing Environment\nYour choice: """))
    if int(choice) == 1:
        print('\nGenerating keys for Aseyev and Balentin...')
        Key_Generator(256)
        print('Key values for Aseyev:\np - ', pq[2], '(', hex(pq[2]), ')\nq - ', pq[3], '(', hex(pq[3]), ')\nn - ',
              A_open_key[1], '\ne - ', A_open_key[0], '\nd - ', A_secret_key[0])
        print('Key values for Balentin:\np - ', pq[0], '(', hex(pq[0]), ')\nq - ', pq[1], '(', hex(pq[1]), ')\nn - ',
              B_open_key[1], '\ne - ', B_open_key[0], '\nd - ', B_secret_key[0])
        k= randint(1,100000000000)
        print('\nSecret key-info from Aseyev equals ', k)
        c = Encrypt(k, A_open_key)
        print('Secret key-message has been encrypted and now equals ', c, '\nNow let`s decrypt it!')
        m = Decrypt(c, A_secret_key)
        print('Secret key-message has been decrypted and now equals ', m)
        k = randint(1, 100000000000)
        print('\nSecret key-info from Balentin equals ', k)
        c = Encrypt(k, A_open_key)
        print('Secret key-message has been encrypted by Balentin and now equals ', c, '\nNow let`s decrypt it!')
        m = Decrypt(c, A_secret_key)
        print('Secret key-message has been decrypted and now equals ', m)
        k = 42
        sm = Send_Key(k, A_secret_key, B_open_key)
        print('\nAseyev has created a message "', k, '" and sent it to Balentin')
        if Receive_Key(sm, B_secret_key, A_open_key):
            print('Balentin has successfully received the message from Aseyev!')
        else:
            print('Balentin has not received the message from Aseyev! :( ')
        choice_end = int(input('\nWant to go back to the beginning?\n1 --- Yes\n2 --- No\nYour choice: '))
        if choice_end == 1:
            Menu()
        else:
            return 0
    if int(choice) == 2:
        print('\nVisit http://asymcryptwebservice.appspot.com to use this feature\n')
        global Server_open_key
        Server_open_key = []
        Server_open_key.append(int(input('Input the server`s e(Public exponent) value: '), 16))
        Server_open_key.append(int(input('Input the server`s n(Modulus) value: '), 16))
        Key_Generator(256)
        print('\nYour key values:\np - ', pq[0], '(', hex(pq[0]), ')\nq - ', pq[1], '(', hex(pq[1]), ')\nn - ',
              B_open_key[1], '\ne - ', B_open_key[0], '\nd - ', B_secret_key[0])
        print('\nYour n(Modulus) equals ', hex(B_open_key[1]))
        print('Your e(Public exponent) equals ', hex(B_open_key[0]))
        key = 1337
        print('\nSharing key is ', key)
        sms = Send_Key(key, B_secret_key, Server_open_key)
        print('Key has been sent to the server!\ns1(Signature) = ', hex(sms[0]), '\nk1(Key) = ', hex(sms[1]))
        choice_end = int(input('\nWant to go back to the beginning?\n1 --- Yes\n2 --- No\nYour choice: '))
        if choice_end == 1:
            Menu()
        else:
            return 0
    else:
        print('There is no option "', choice, '". Please, try again')
        return Menu()


Menu()
