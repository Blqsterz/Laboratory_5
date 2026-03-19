while True:
    word = input("Введите слово для проверки на редкость ")
    word = word.lower() 

    if word == "стоп":
        break

    letters = list(word)
    letter_rare = False
    
    for letter in letters:
        if letter == "ф":
            letter_rare = True 
            break 
    if letter_rare:
        print("Ого! Это редкое слово!")
    else:    
        print("Эх, это не очень редкое слово...")