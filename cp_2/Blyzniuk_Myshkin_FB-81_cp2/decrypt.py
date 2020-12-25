from funcs import *

file = open(os.path.join(sys.path[0], 'encrypted.txt'), 'r', encoding='UTF-8')  # Open file with encrypted text
w_file = open(os.path.join(sys.path[0], 'decrypted.txt'), 'a', encoding='UTF-8')  # Open file to write decrypted text

alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))  # Get russian alphabet
indexed_alphabet = {key: v for v, key in enumerate(alphabet)}  # Enumerate russian alphabet with indexes

text = re.sub(r'\W', '', file.read().lower())  # Read encrypted text from file
indexed_text = list(map(lambda i: indexed_alphabet[i], text))  # Index all the encrypted text with indexes

stat_file = open(os.path.join(sys.path[0], 'statistics_text.txt'), 'r',
                 encoding='UTF-8')  # Open file with large text for statistics
stat_text = re.sub(r'[^А-Яа-я]', '', stat_file.read().lower())  # Read text from the file

reference_dict = entropy_counter(stat_text)  # Get dict with entropy of each letter for statistic

data = key_length(text)  # Get dict with conformity index of each chunk that illustrates possible key length
print("Conformity of text : " + str(conformity_index(text)))  # Print conformity index of encrypted text

print(str(data))  # Print conformity index of each chunk that illustrates possible key length
print(
    "Conformity index of encrypted text: " + str(conformity_index(text)))  # General conformity index of encrypted text
clrs = ['grey' if (x < max(data.values())) else 'red' for x in data.values()]  # Set colors for bars in chart
plt.bar(data.keys(), data.values(), color=clrs)  # Create bar chart of conformity index of each chunk
plt.show()  # Show chart

partial_caesar_decryptor(text, reference_dict, 14)  # Decrypt every chunk with known key length got from charts
decrypted_text = decryptor('последнийдозор', indexed_text,
                           indexed_alphabet)  # Decrypt text with key got from decrypting and analyznig every chunk
w_file.write(" ".join(wordninja.split(decrypted_text)))  # Write decrypted text in file, splitting by words

file.close()  # Close file with encrypted text
w_file.close()  # Close file with decrypted text
stat_file.close()  # Close file with text for statistics
