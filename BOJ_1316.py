n = int(input())



count = 0
for _ in range(n):
    isWord = True
    word = input()
    check_list = []
    for i in range(len(word)):
        if not check_list:
            check_list.append(word[i])
            #이새끼땜에 골머리썩음
            continue
        
        if word[i] in check_list:
            if word[i] == word[i-1]:
                continue
            else:
                isWord = False
                break
        else:
            check_list.append(word[i])
    if isWord:
        count+=1
print(count)