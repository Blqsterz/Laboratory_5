words = []

while True:
    word = input(f"Введите слова: ")
    words.append(word)

    if word.lower() == "stop":
        break

words.remove("stop")
result = " ".join(words)   
print(result)