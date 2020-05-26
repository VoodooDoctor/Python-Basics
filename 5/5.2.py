f = open("Text5.2.txt", 'r')
lines = 0
for i in f:
    lines +=1

    l = 0
    words = 0
    for n in i:
        if n != ' ' and l == 0:
            words += 1
            l = 1
        elif n == ' ':
            l = 0
    print(words, 'сл.')


print(lines, 'стр.')
f.close()