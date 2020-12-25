from typing import List, Dict, Tuple, IO, Any
from sys import stdout
from collections import Counter
import logging
from pprint import pprint
sh = logging.StreamHandler(stdout)
fh = logging.FileHandler('report.txt', 'w') 
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=(sh, fh))

most_used_letters = [ 'о','е','а','н','и','т','с','л','в','р','к','д','м','у','п','я','ь','ы','г','б','ч','з','ж','й','ш','х','ю','э','щ','ц','ф','ъ','ё']
ciphertext_f = open('./cp_2/kozachok-fb82_kuznetsov-fb82_cp_2/ciphertext.txt', 'r')
myopentext_anna_f = open('./cp_2/kozachok-fb82_kuznetsov-fb82_cp_2/anna.txt', 'r')
myopentext_anna_begining_f = open('./cp_2/kozachok-fb82_kuznetsov-fb82_cp_2/anna_begining.txt')

keys_different_length = [
    "ку",                   #2
    "мда",                  #3
    "мама",                 #4
    "арбат",                #5
    "приветкотя",           #10
    "анатолийдед",          #11
    "светочеймоих",         #12
    "велосипедвага",        #13
    "моршинскаявода",       #14
    "макбукпрокрутой",      #15
    "работатьмневкайф",     #16
    "силаджедаявагабун",    #17
    "ноутбукисиладжедая",   #18
    "читаймеждустрокбрат",  #19
    "строкинестрокибезума"  #20
]

class Vigenere():

    letters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    
    l_n = { letter: number for number, letter in enumerate(letters) }
    n_l = { number: letter for number, letter in enumerate(letters) }

    def __init__(self, text: str=None, f: IO[Any]=None, key: str=None):
        self.key = key
        try:
            self.text = self.filter_text(text.lower())
        except TypeError:
            self.text = None
        self.f = f

    def check_crypt(self) -> bool:
        if self.text is None and self.f is None:
            logging.info("Pass only file or only text")
            return False
        
        if self.key is None:
            logging.info("Decryption/Encryption only can be performed when key is not NONE") 
            return False
        return True

    def check_crack(self) -> bool:
        return True
    
    @staticmethod
    def filter_text(text: str) -> str:
        filtered_letters = []

        for letter in text:
            if letter in Vigenere.letters:
                filtered_letters.append(letter)

        return "".join(filtered_letters)

    def __proc_text(self, mode: str) -> str:
        n_l = Vigenere.n_l
        l_n = Vigenere.l_n
        processed_text_list = []
        key_len = len(self.key)
        
        if self.text is None:
            try:
                self.text = self.filter_text(self.f.read())
            except AttributeError:
                logging.error("Instead of filetype was passed another type")
                return ""

        self.text = self.text.lower()

        if mode == 'e':
            for i, letter in enumerate(self.text):
                letter_number = (l_n[letter] + l_n[self.key[i % key_len]]) % len(Vigenere.letters)
                processed_text_list.append(n_l[letter_number])
        
        else:
            for i, letter in enumerate(self.text):
                letter_number = (l_n[letter] - l_n[self.key[i % key_len]]) % len(Vigenere.letters)
                processed_text_list.append(n_l[letter_number])

        return "".join(processed_text_list)


    def encrypt(self) -> str:
        if not self.check_crypt():
            logging.info("Encryption cannot be performed")

        return self.__proc_text('e')

    def decrypt(self) -> str:
        if not self.check_crypt():
            logging.info("Decryption cannot be performed")

        return self.__proc_text('d')

    def count_indicies(self) -> str:
        "Returns string for excel table"
        Indices = {}
        s = ""
        # Подсчёт индексов
        for r in range(2, 35):
            Y =  self.text[::r] 
            letter_number = Counter(Y)
            summ = 0
            for letter, number in letter_number.items():
                summ += number * (number - 1)
            l = len(Y)
            I = summ / (l * (l - 1))
            Indices[r] = I

        sIndices = sorted(list(Indices.items()), key=lambda x: x[0], reverse=True)
        for r, I in sIndices:
            print("Key length: {r}, Index: {I:3>}".format(r=r, I=str(I)) )
            s += "{r}\t{I:3>}\n".format(r=r, I=str(I))
        return s


    def crack(self, key_len: int) -> str:
        if not self.check_crack():
            return

        general_key = ""
        for i in range(key_len):
            Yi = self.text[i::key_len]
            letter = Counter(Yi).most_common(1)[0][0]
            int_let = Vigenere.l_n[letter]
            k = (int_let - Vigenere.l_n[most_used_letters[0]]) % len(Vigenere.l_n)
            open_letter = Vigenere.n_l[k]
            general_key += open_letter

        print("Cracked_key:", general_key)
        return general_key

        logging.info("Pass more text to get more accurate result")

        
def crack_variant_9():
     
    # Read ciphertext to crack
    ciphertext = ciphertext_f.read()

    # Create object
    ve_obj = Vigenere(ciphertext)

    # Show idecies of conformity sorted descending
    ve_obj.count_indicies()
    
    # Get cracked (or almost cracked key)
    key = ve_obj.crack(17)
    print(key)

    # Recreate our ve_obj with key to decipher text
    ve_obj = Vigenere(ciphertext, key='войнамагаэндшпиль')
    
    # Print 100 decrypted characters and save all output to file
    print((decrypted_text := ve_obj.decrypt())[:100])
    with open('./cp_2/kozachok-fb82_kuznetsov-fb82_cp_2/decrypted_text.txt', 'w') as f:
        f.write(decrypted_text)

def encrypt_and_count_indecies():
    # --- TEST WITH ANNA KARENINA ---
    plaintext = myopentext_anna_begining_f.read()
    # with open("./cp_2/kozachok-fb82_kuznetsov-fb82_cp_2/report.txt", 'w') as f: pass
    for key in keys_different_length:
        report_file = open("./cp_2/kozachok-fb82_kuznetsov-fb82_cp_2/report_{}.txt".format(len(key)), 'w')
        print(' --- Key: {}'.format(key))
        obj = Vigenere(plaintext, key=key)
        # print( (enc:=obj.encrypt())[:100], '\n')
        obj = Vigenere(obj.encrypt())
        report_file.write(key + '\n')
        report_file.write(obj.count_indicies().replace('.', ','))

if __name__ == '__main__':

    encrypt_and_count_indecies()

    # crack_variant_9()
   

    



    
    