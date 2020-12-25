from functions.functions import *
import itertools

# read ciphertext from file
f=open('text/12.txt', 'r')
line=''.join(f.readlines()).replace('\n', '')
f.close()

# get five most often bigrams
x=sort_dict(count_bigrams(line, False))
first_elements = [i[0] for i in list(x.items())[:5]]

# set flag to 0 (change it if plaintext found)
flag = 0

# go thought every possible combination of
# (2 bigrams from most often in language, 2 bigrams from most often in ciphertext)
for i in itertools.permutations(five_most_often, 2):
    for j in itertools.combinations(first_elements, 2):
        print('-> X: '+str(i)+'; Y: '+str(j)+';')

        # get coefficients for decryption, check if not None
        a, b=get_coefs(i, j)
        if len(a)<1:
            print('      error: coef a does not exist')

        # go thought every pair (a, b) for decryption
        for (ael, bel) in zip(a, b):
            print('   a: '+str(ael)+'; b: '+str(bel) )
            plaintext = decipher_afin_bigrams(ael, bel, line)

            # check if plaintext follows the criteria
            # and if inverse of a exists (if it does, len(plaintext) will be >0)
            if len(plaintext)>0 and is_plaintext(plaintext):
                print('      plaintext: '+plaintext[:100]+'...')

                # write plaintext to file and change flag to 1
                if flag==0:
                    fileout = open('results/decrypted_12.txt', 'w')
                    fileout.write(plaintext)
                    fileout.close()
                    flag+=1

                    #exit() # uncomment to end program on first plaintext found
        print()
