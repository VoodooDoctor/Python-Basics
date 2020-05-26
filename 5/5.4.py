rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []

with open('Text5.4.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('Text5.4_new.txt', 'w') as f2:
    f2.writelines(new_file)