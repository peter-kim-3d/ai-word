words = "1. Apple\n2. Amazing\n3. Always"
words_list = [word.split('. ')[1] for word in words.split('\n')]
print(words_list)