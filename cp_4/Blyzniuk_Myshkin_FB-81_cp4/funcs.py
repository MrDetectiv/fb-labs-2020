import random


def gcd(first_number, second_number):
    coefs = []
    # print("gcd of " + str(first_number) + " and " + str(second_number), end=" is ")
    while second_number != 0:
        t = second_number
        if first_number > second_number:
            coefs.append(first_number // second_number)
        second_number = first_number % second_number
        first_number = t
    # print(first_number)
    return first_number, coefs


def find_opposite(a, mod):
    _, coefs = gcd(a, mod)
    # print("coefs: " + str(coefs))
    x = 1
    y = 0
    t = 0
    for index in range(0, (len(coefs) - 1)):
        t = x
        x = x * -(coefs[index]) + y
        y = t
    if x < 0:
        x = x + mod
    # print("opposite is: " + str(x))
    return x


def has_common_divider(a, b):
    if gcd(a, b)[0] > 1:
        return True
    else:
        return False


def left_to_right_power(a, power, mod): # https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B_%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B3%D0%BE_%D0%B2%D0%BE%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B2_%D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B_%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B7%D0%B0%D0%B4%D0%B0%D1%87
    bin_pow = bin(power)[2:]  # removing "0b" and than reversing string
    y = 1
    for i in range(len(bin_pow)):
        if i == len(bin_pow)-1:
            y = y * (a ** int(bin_pow[i]))
        else:
            y = (y * (a ** int(bin_pow[i]))) ** 2
        y = y % mod
    return y


def random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)


def key_hex(key):
    res = []
    for i in range(len(key)):
        res.append(hex(key[i]))
    return res


def site_hex(m):
    return hex(m)[0] + hex(m)[2:]


def site_key_hex(key):
    res = []
    for i in range(len(key)):
        res.append(site_hex(key[i]))
    return res


def random_prime(key_length):
    lower_bound = 2 ** key_length
    upper_bound = 2 ** (key_length + 1) - 1
    # print("Looking for random number in range " + str(lower_bound), str(upper_bound))
    rand_number = random_number(lower_bound, upper_bound)
    while True:
        if rand_number >= (upper_bound-2):
            rand_number = random_number(lower_bound, upper_bound)

        if rand_number % 2 == 0:
            rand_number += 1

        if miller_rabin_test(rand_number):
            # print("We found a prime number: " + str(rand_number))
            break
        else:
            # print("Rabin says " + str(rand_number) + " is not prime number")
            # so add 2
            rand_number += 2
    return rand_number


def miller_rabin_test(number):
    k = 100
    d = number - 1
    s = 0
    # number-1 = d * 2^(s) -> d = (number-1) / 2^(s)
    # s - количество двоек в разложении (number - 1)
    while d % 2 == 0:
        s += 1
        d = d // 2  # d = (d - (d % 2)) /2

    for _ in range(k):
        # take random x in range 1 < x < number OR 2 <= x <= (number-1)
        x = random_number(2, number - 1)
        if gcd(x, number)[0] > 1:
            # number is not prime
            return False
        x = left_to_right_power(x, d, number)
        if x == 1 or x == (number - 1):  # x == -1
            # sil`no psevdoprostoe za osnovaniem x
            continue
        else:
            # number can be prime or not
            pseudo_prime = False

            for si in range(1, s):
                # x_r = x^(d * 2^(si)) -> x^(d) * x^(2^si)
                x_r = x * left_to_right_power(x, 2 ** si, number)

                if x_r == number - 1:  # x == -1
                    # sil`no psevdoprostoe za osnovaniem x
                    pseudo_prime = True
                elif x_r == 1:
                    # ne sil`no psevdoprostoe za osnovaniem x
                    return False

            if not pseudo_prime:
                # number is composite number (number = p * q)
                return False

    return True
