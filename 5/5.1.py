with open("Text1.txt", "w+") as f:
    line = input('Введите текст \n')
    while line:
        f.writelines(line)
        line = input('Введите текст \n')
        if not line:
            break

    content = f.read()
print(content)