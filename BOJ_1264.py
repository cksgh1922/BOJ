while True:
    word = input()
    
    word = word.lower()
    stop = False
    count = 0
    for char in word:
        if char == "i" or char == "a" or char == "e" or char == "o" or char == "u":
           count+=1
        elif char == "#":
            stop = True
            break
    if stop:
        break
    else:
        print(count)
    
     