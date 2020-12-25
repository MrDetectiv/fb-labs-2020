import random


def random_int(min, max):
    # random int in min <= a <= max
    return random.randint(min, max)


def random_prime(min_number, max_number):
    random_number = random_int(min_number, max_number)
    # if number is even -> +1
    # if number is odd -> do nothing
    if not odd(random_number):
        random_number += 1

    while True:
        # if number is prime -> return it
        # if number is not prime -> +2 and continue loop
        if is_prime(random_number):
            return random_number
        else:
            random_number += 2


def random_prime_bit(bit_lenght):
    # 1000....0000
    # min_number has "1" at the start and (bit_lenght - 1) "0"
    min_number = 2 ** (bit_lenght // 2 - 1)
    # 1111....1111
    # max_number has (bit_length) "1"
    max_number = 2 ** (bit_lenght // 2 + 1) - 1
    return random_prime(min_number, max_number)


def gcd(first_num, second_num):
    if second_num == 0:
        return first_num
    else:
        return gcd(second_num, first_num % second_num)


# Miller-Rabin primality test
def is_prime(n):
    # prevent potential infinite loop when d = 0
    if n < 2:
        return False

    # Decompose (n - 1) to write it as (2 ** r) * d
    # While d is even, divide it by 2 and increase the exponent.
    k = 1024
    d = n - 1
    r = 0

    while not (d & 1):
        r += 1
        d >>= 1

    # Test k witnesses.
    for _ in range(k):
        # Generate random integer a, where 2 <= a <= (n - 2)
        a = random_int(2, n-2)

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                print(f"Miller Rabin failure(composite): {n}")
                # n is composite.
                return False
            if x == n - 1:
                # Exit inner loop and continue with next witness.
                break
        else:
            print(f"Miller Rabin failure(composite): {n}")
            # If loop doesn't break, n is composite.
            return False
    print(f"Miller Rabin approve ( prime ) : {n}")
    return True


def odd(number):
    return number % 2 == 1


def opposite(a, mod):
    coefficients = []
    f_number = a
    s_number = mod
    while s_number != 0:
        temp = s_number
        if f_number > s_number:
            coefficients.append(f_number // s_number)
        s_number = f_number % s_number
        f_number = temp


    x1 = 1
    x0 = 0
    temp = 0
    for i in range(len(coefficients) - 1):
        temp = x1
        x1 = x1 * -coefficients[i] + x0
        x0 = temp
    if x1 < 0:
        x1 = x1 + mod
    return x1
