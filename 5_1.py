num = (int(input("Введите количество вводимых слов: ")))
words = []

for i in range(num):
    word = input(f"Введите слово под номером {i+1}: ")
    words.append(word)

result = " ".join(words)   
print(result)