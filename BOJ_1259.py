while True:
    n = input()
    yesorno = True
    if n == "0":
        break
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]:
            yesorno = False
            break
        
    print("yes" if yesorno else "no")