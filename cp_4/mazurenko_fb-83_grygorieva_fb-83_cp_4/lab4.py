import random

# euclidean algorithm
def euclid_algorithm(a, b):
    if a < b:
        if b % a == 0:
            return a
        else:
            return euclid_algorithm(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return euclid_algorithm(b, a % b)
            
# extended euclidean algorithm
def extended_euclids_algo(a, b):
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    while b:
        q = a // b
        #u_(i+1) = u_(i-1) - q_(i)*u_(i)
        #v_(i+1) = v_(i-1) - q_(i)*v_(i)
        u1, u0 = u0 - q*u1, u1
        v1, v0 = v0 - q*v1, v1
        a, b = b, a % b
    return a, u0, v0

# modular multiplicative inverse
def mod_multi_inverse(a, m):
    gcd, u, v = extended_euclids_algo(a, m)
    if (gcd == 1):
        # a*u = 1 % m
        return u

def representation_of_number(number):
  n = number
  s = 0
  while (n % 2 == 0):
    s += 1
    n -= n // 2
  d =  number // pow(2, s)
  return s, d

def search_random_prime_number(bits, k):
    #p = random.getrandbits(bits)
    p = random.getrandbits(bits-1) + (1 << bits-1)
    if (p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0 and p % 11 != 0):
        s, d = representation_of_number(p - 1)
        counter = 0
        while (counter != k):
            x = random.randint(1, p)
            gcd = euclid_algorithm(x, p)
            if (gcd > 1):
                return 0
            else:
                answer = 0
                if ((pow(x, d, p) == 1) or (pow(x, d, p) == p - 1)):
                    answer = 1
                else:
                    if (s == 1):
                        Xr = pow(x, d * 2, p)
                        if (Xr == p - 1):
                            answer = 1
                        else:
                            return 0
                    else:
                        for r in range(1, s - 1):
                            Xr = pow(x, d * pow(2, r), p)
                            if (Xr == p - 1):
                                answer = 1
                            elif (Xr == 1):
                                return 0
                            else:
                                answer = 0
                if (answer == 1):
                    #print("gcd(p,x) = gcd(" + str(p) + "," + str(x) + ") = " + str(gcd))
                    counter += 1
                else:
                    return 0
        if (counter == k):
            text = "p - 1 = d*pow(2,s) = " + str(d) + "*pow(2," + str(s) + ")" + '\n'
            return p
        else:
            #print("MILLER-RABIN TEST FAILED FOR ", p)
            return 0
    else:
        #print("DIVISION TEST BY 2,3,5,7 OR 11 FAILED FOR ", p)
        return 0

def rsa_system_build(p, q):
    n = p * q
    Fn = (p - 1) * (q - 1)
    e = random.randint(2, Fn - 1)
    while (euclid_algorithm(e, Fn) != 1):
         e = random.randint(2, Fn - 1)
    d = mod_multi_inverse(e, Fn)
    #check = (d * e) % Fn
    #print("check =", check)
    if (d < 0):
        d = d % Fn
    text = "(e,n,d) = (" + str(e) + "," + str(n) + "," + str(d) + ")" + '\n'
    return e, n, d

def encrypt(m, e, n):
    c = pow(m, e, n)
    return c

def decrypt(c, d, n):
    m = pow(c, d, n)
    return m

def sign(m, d, n):
    s = pow(m, d, n)
    return (m, s)

def verify(m_s, e, n):
    if(m_s[0] == pow(m_s[1], e, n)):
        return True
    else:
        return False

def find_number_for_user(bits, k):
  number = search_random_prime_number(bits, k)
  while (number == 0):
    number = search_random_prime_number(bits, k)
    if (number != 0):
      break
  return number

def user_choose(user):
  k = 100
  print("HOW many bits for user", user, "do you want to generate?")
  bits = input()
  bits = int(bits)
  p = find_number_for_user(bits, k)
  q = find_number_for_user(bits, k)
  print("GENERATED for user", user, ":", "\n p =", hex(p), "\nq =", hex(q))
  return rsa_system_build(p, q)

def user_interaction_with_functions(user_name):
    user = user_choose(user_name)
    #print("(e,n,d) for user A looks like this:\n", user)
    print("\n\n(e,n,d) for user", user_name, "looks like this:\n", "(", hex(user[0]), ",", hex(user[1]), ",", hex(user[2]), ")")
    
    message = random.randint(pow(2, 127), pow(2, 128))
    print("\nMessage looks like: ", hex(message))
    cipher_text = encrypt(message, user[0], user[1])
    print("\nEncrypted message: ", hex(cipher_text))

    open_text = decrypt(cipher_text, user[2], user[1])
    print("\nDecrypted message: ", hex(open_text))

    signed_message = sign(message, user[2], user[1])
    print("\nSignature (", hex(signed_message[0]), "~", hex(signed_message[1]), ") generated for message")

    verification = verify(signed_message, user[0], user[1])
    if(verification == True):
        print("\nMessage verification done")
    else:
        print("\nMessage NOT verified")
    print("\n================================================================================================\n")
    return user

def send_key(user_a, e1, n1, key):
    e = user_a[0]
    n = user_a[1]
    d = user_a[2]
    s = decrypt(key, d, n)
    k1 = encrypt(key, e1, n1)
    s1 = encrypt(s, e1, n1)
    return k1, s1

def receive_key(k1, s1, user_b, user_a):
    e = user_a[0]
    n1 = user_b[1]
    n = user_a[1]
    d1 = user_b[2]
    k = decrypt(k1, d1, n1)
    s = decrypt(s1, d1, n1)
    return sign(s, e, n)

def user_a_and_b_interaction(user_a, user_b):
    print("LET`S ORGANISE COMMUNICATION BETWEEN A AND B")
    if(user_b[1] >= user_a[1]):
        #print("\n\n###", user_a[1], user_b[1], "\n\n")
        key = random.randint(1, user_a[1] - 1)
        print("USER A PICKS UP THIS KEY: ", hex(key))
        k1, s1 = send_key(user_a, user_b[0], user_b[1], key)
        verification = receive_key(k1, s1, user_b, user_a)
        if(verification[1] == key):
            print("SHARED KEY BETWEEN A AND B ESTABLISHED SUCCESSFULLY!!!")
            print(hex(key))
            return key
        else:
            print("ERROR ON DELEVERING KEY FROM A TO B...")
            print("???", hex(verification))
            return False
    else:
        print("REGENERATING USER`S A DATA: n1<n")
        #print("\n\n!!!", user_a[1], user_b[1], "\n\n")
        while(user_a[1] > user_b[1]):
            user_a = user_interaction_with_functions("A")
            if(user_b[1] >= user_a[1]):
                user_a_and_b_interaction(user_a, user_b)
                break

def user_a_and_b_interaction(user_a, user_b):
    print("LET`S ORGANISE COMMUNICATION BETWEEN A AND B")
    if(user_b[1] >= user_a[1]):
        #print("\n\n###", user_a[1], user_b[1], "\n\n")
        key = random.randint(1, user_a[1] - 1)
        print("USER A PICKS UP THIS KEY: ", hex(key))
        k1, s1 = send_key(user_a, user_b[0], user_b[1], key)
        verification = receive_key(k1, s1, user_b, user_a)
        if(verification[1] == key):
            print("SHARED KEY BETWEEN A AND B ESTABLISHED SUCCESSFULLY!!!")
            print(hex(key))
            return key
        else:
            print("ERROR ON DELEVERING KEY FROM A TO B...")
            print("???", hex(verification))
            return False
    else:
        print("REGENERATING USER`S A DATA: n1<n")
        #print("\n\n!!!", user_a[1], user_b[1], "\n\n")
        while(user_a[1] > user_b[1]):
            user_a = user_interaction_with_functions("A")
            if(user_b[1] >= user_a[1]):
                user_a_and_b_interaction(user_a, user_b)
                break

def user_and_server_interaction(user_a):
    print("\n\nEnter public key for server: first e1:")
    e1 = input()
    e1 = int(e1, 16)
    print("e1 = ", e1)
    print("then n1:")
    n1 = input()
    n1 = int(n1, 0)
    print("n1 = ", n1)
    print("LET`S ORGANISE COMMUNICATION BETWEEN A AND B")
    if(n1 >= user_a[1]):
        print("\n\n###", user_a[1], n1, "\n\n")
        key = "777"
        key = int(key)
        print("USER A PICKS UP THIS KEY: ", hex(key), "/", key)
        k1, s1 = send_key(user_a, e1, n1, key)
        s = pow(key, user_a[2], user_a[1])
        print("USER A COUNTED s = ", hex(s))
        return k1, s1
    else:
        print("\n\n!!!", user_a[1], n1, "\n\n")
        while(user_a[1] > n1):
            user_a = user_interaction_with_functions("A")
            if(n1 >= user_a[1]):
                user_and_server_interaction(user_a)
                #break

def main():
    user_a = user_interaction_with_functions("A")
    user_b = user_interaction_with_functions("B")

    result = user_a_and_b_interaction(user_a, user_b)
    print(result)
    if(result != False and result != None):
        print(hex(result))

    data_for_server = user_and_server_interaction(user_a)
    print("Key for server (k1) =", hex(data_for_server[0]))
    print("Signature for server (s1) =", hex(data_for_server[1]))
    print("User`s A n = ", hex(user_a[1]))
    print("User`s A e = ", hex(user_a[0]))
    print("User`s A d = ", hex(user_a[2]))

main()
