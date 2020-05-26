with open('Text5.3.txt', 'w+') as f:
    salary = []
    low_salary = []

    new_list = f.read().split('\n')
    for i in new_list:
        i = i.split()
        if int(i[1]) < 20000:
            low_salary.append(i[0])
        salary.append(i[1])

print(f'Сотрудники с окладом меньше 20000 {low_salary}, Средний оклад {sum(map(int,salary)) / len(salary)}')
