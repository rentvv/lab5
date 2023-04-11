import random
def z1():
    num = [3, 4, 7, 6, 1, 9]
    x = int(input())
    if x in num:
        print("поздравляем вы угадали число")
    else:
        print("к сожалению вы не угадали")

def z2():
    num = [1, 4, 4, 6, 3, 5, 7, 7]
    for i in num:
        if num.count(i)>1:
            print(i)

def z3():
    ned=("понедельник","вторник","среда","четверг","пятница","суббота","воскресенье")
    d = int(input("сколько выходных вы хотите?"))
    for i in ned:
        print("ваши рабочие дни", ned[:-d])
        print("ваши выходные дни", ned[-d:])
        break

def z4():
    g1 = ["Вавилов","Максимов","Федоров","Дмитривев"]
    g2= ["Молотков", "Иванов", "Топоров", "Фролов"]
    a = []
    for i in range(2):
        a.append(g1[random.randint(0,3)])
        a.append(g2[random.randint(0, 3)])
    print("первая группа " , *g1)
    print("вторая группа ", *g2)
    print(*tuple(sorted(a)))
    print(len(a))
    print([f'иванов встречается в кортеже: {a.count("Иванов")}', 'Иванова нет'][0 if a.count("Иванов")>0 else 1])


z1()
z2()
z3()
z4()