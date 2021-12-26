article = open("artykul.txt", "r", encoding="utf-8")

content = article.read()
sentences = [""]
words = content.split()

for i in range(len(words) - 2):
    sentences[-1] = sentences[-1] + ' ' + words[i]
    if words[i][-1] in ['.', '?', '!'] and words[i + 1][0].isupper():
        sentences.append("")


print("Ilość zdań:", len(sentences))
for s in range(len(sentences)):
    print(f"Ilość słów w zdaniu {s + 1}: {len(sentences[s].split())}")
