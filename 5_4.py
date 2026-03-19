print("ИГРА 'МАТЕМАТИКА ДЛЯ ДЕТЕЙ'")
import random
mistakes = 0
corrects = 0

while mistakes < 3:

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)

    answer = int(input(f"{num1}+{num2}= "))
    correct_answer = num1 + num2
    
    if answer == correct_answer:
        print("Правильно!")
        corrects = corrects + 1
    else:
        print("Ответ неверный")
        mistakes = mistakes + 1

print(f"Игра окончена. Правильных ответов:{corrects}")