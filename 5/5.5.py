def calc():
    with open('Text5.5.txt', "w+") as f:
        line = input('Введите числа через пробел \n')
        f.writelines(line)
        f2 = line.split()
    print(sum(map(int, f2)))
calc()
