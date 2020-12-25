from funcs import *

file = open(os.path.join(sys.path[0], 'text.txt'), 'r', encoding='UTF-8')  # Open file with clear text to encrypt
w_file = open(os.path.join(sys.path[0], 'text_encrypted.txt'), 'a',
              encoding='UTF-8')  # Open file to write encrypted text

text = re.sub(r'\W', '', file.read().lower())  # Get clear text from file

alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))  # Get russian alphabet
indexed_alphabet = {key: v for v, key in enumerate(alphabet)}  # Enumerate russian alphabet with indexes

keys = ['да', 'кот', 'лорд', 'салат', 'вкусныйвидеосалат']  # Set keys that will be used to encrypt data

indexed_text = list(map(lambda i: indexed_alphabet[i], text))  # Index all the clear text with indexes

print("Conformity index of clear text: " + str(conformity_index(text)))  # Get conformity index of clear text

for i in range(0, len(keys)):
    encrypted_text = encryptor(keys[i], indexed_text, indexed_alphabet)  # Encrypt text with one of the keys
    encrypted_text_conformity = conformity_index(encrypted_text)  # Count conformity index of encrypted text
    keys_conformity = key_length(encrypted_text)  # Get dict with conformity index of each chunk that illustrates
    # possible key length
    print(str("\n" + "KEY: " + keys[i] + "\n\n" + encrypted_text + "\n\n" + str(
        keys_conformity) + "\n"))  # Print encryption key, encrypted text and conformity indexes of chunks
    # w_file.write(str("\n\n" + "KEY: " + keys[i] + "\n" + encrypted_text + "\n\n")
    print("Conformity index of encrypted text: " + str(conformity_index(encrypted_text))) # General conformity index
    # of encrypted text
    clrs = ['grey' if (x < max(keys_conformity.values())) else 'red' for x in
            keys_conformity.values()]  # Set colors for bars in chart
    plt.bar(keys_conformity.keys(), keys_conformity.values(),
            color=clrs)  # Create bar chart of conformity index of each chunk
    plt.show()  # Show chart

file.close()
w_file.close()
