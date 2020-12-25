text = open("filtered_text.txt", 'r', encoding='utf8')
text1 = open("filtered_text_without_spaces.txt", 'w', encoding='utf8')
text2 = ""
for line in text:
    newline = line.replace(" ", "")
    text2 += newline
text1.write(text2)