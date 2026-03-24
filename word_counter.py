import matplotlib.pyplot as plt

paragraph = """" """

normalised = paragraph.lower()

punctuation = ".!?,"


removed = str.maketrans({char: None for char in punctuation})

cleaned_txt = normalised.translate(removed)

print (cleaned_txt)

words = cleaned_txt.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
   
sorted_words = sorted(word_count.items(), key = lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word + ":", count)
    

top_n = int(input("How many top words to display? "))
top_words = sorted_words[:top_n]

words_counted = [word for word, count in sorted_words]
count = [count for word, count in sorted_words]

plt.figure()
plt.xticks(rotation=45)
plt.bar(words_counted, count)

        