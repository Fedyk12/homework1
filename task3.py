words = ["кот", "пёс", "кот", "кот", "ёж", "пёс", "кот"]

data = {}
for word in words:
	data[word] = data.get(word,0) + 1
count_words = []
for key in data:
	count_words.append([key,data[key]])
count_words = sorted(count_words)
for slovo in range(len(count_words)):
	print(f'{slovo+1}.',count_words[slovo][0],'-',count_words[slovo][1])


