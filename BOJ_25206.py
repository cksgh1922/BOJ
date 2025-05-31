def alphabetToInt(alphabet):
    if alphabet == "A+":
        alphabet = 4.5
    elif alphabet == "A0":
        alphabet = 4.0
    elif alphabet == "B+":
        alphabet = 3.5
    elif alphabet == "B0":
        alphabet = 3.0
    elif alphabet == "C+":
        alphabet = 2.5
    elif alphabet == "C0":
        alphabet = 2.0
    elif alphabet == "D+":
        alphabet = 1.5
    elif alphabet == "D0":
        alphabet = 1.0
    elif alphabet == "P":
        pass
    elif alphabet == "F":
        alphabet == 0
    return alphabet



score_dic = {}

for _ in range(3):
    n,score,alphabet = map(str,input().split())
    alphabet = alphabetToInt(alphabet)
    score_dic[float(score)] = alphabet

print(score_dic)